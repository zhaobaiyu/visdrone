import torch
import torch.nn as nn
import torch.nn.functional as F
# from torch.autograd import Variable
import numpy as np
from util import *


# parsing the configuration file
def parse_cfg(cfgfile):
    
    file = open(cfgfile, 'r')
    lines = file.read().split('\n')
    lines = [x for x in lines if len(x) > 0]
    lines = [x for x in lines if x[0] != '#']
    lines = [x.rstrip().lstrip() for x in lines]
    
    block = {}
    blocks = []
    
    for line in lines:
        # if the start of a new block
        if line[0] == '[':
            if len(block) != 0:
                blocks.append(block)
                block = {}
            block['type'] = line[1:-1].rstrip()
        else:
            key, value = line.split('=')
            block[key.rstrip()] = value.lstrip()
            
    blocks.append(block)
    
    return blocks


# creating the building blocks
class EmptyLayer(nn.Module):
    def __init__(self):
        super(EmptyLayer, self).__init__()
        
class DetectionLayer(nn.Module):
    def __init__(self, anchors):
        super(DetectionLayer, self).__init__()
        self.anchors = anchors

def create_modules(blocks):
    net_info = blocks[0]
    module_list = nn.ModuleList()
    prev_filters = 3
    output_filters = []
    
    for index, x in enumerate(blocks[1:]):
        module = nn.Sequential()
        
        # check the type of block
        # create a new module for the block
        # append to module_list
        
        ### conv
        if (x['type'] == 'convolutional'):
            activation = x['activation']
            try:
                batch_normalize = int(x['batch_normalize'])
                bias = False
            except:
                batch_normalize = 0
                bias = True
                
            filters = int(x['filters'])
            padding = int(x['pad'])
            kernel_size = int(x['size'])
            stride = int(x['stride'])
            
            if padding:
                pad = (kernel_size - 1) // 2
            else:
                pad = 0
            
            # add the convolutional layer 
            conv = nn.Conv2d(prev_filters, filters, kernel_size, stride, pad, bias=bias)
            module.add_module('conv_{}'.format(index), conv)
            
            # add the batch norm layer
            if batch_normalize:
                bn = nn.BatchNorm2d(filters)
                module.add_module('batch_norm_{}'.format(index), bn)
                
            # check the activation
            if activation == 'leaky':
                activn = nn.LeakyReLU(0.1, inplace=True)
                module.add_module('leaky_{}'.format(index), activn)
                
        ### upsampling layer
        elif x['type'] == 'upsample':
            stride = int(x['stride'])
            upsample = nn.Upsample(scale_factor=2, mode='bilinear')
            module.add_module('upsample_{}'.format(index), upsample)
            
        ### route layer
        elif x['type'] == 'route':
            x['layers'] = x['layers'].split(',')
            # start of a route
            start = int(x['layers'][0])
            # end, if there exists one
            try:
                end = int(x['layers'][1])
            except:
                end = 0
            # positive anotation
            if start > 0:
                start = start - index
            if end > 0:
                end = end - index
            route = EmptyLayer()
            module.add_module('route_{}'.format(index), route)
            if end < 0:
                filters = output_filters[index + start] + output_filters[index + end]
            else:
                filters = output_filters[index + start]
                
        ### shortcut layer
        elif x['type'] == 'shortcut':
            shortcut = EmptyLayer()
            module.add_module('shortcut_{}'.format(index), shortcut)
        
        ### yolo layer
        elif x['type'] == 'yolo':
            mask = x['mask'].split(',')
            mask = [int(x) for x in mask]
            
            anchors = x['anchors'].split(',')
            anchors = [int(a) for a in anchors]
            anchors = [(anchors[i], anchors[i+1]) for i in range(0, len(anchors), 2)]
            anchors = [anchors[i] for i in mask]
            
            detection = DetectionLayer(anchors)
            module.add_module('Detection_{}'.format(index), detection)
        
        module_list.append(module)
        prev_filters = filters
        output_filters.append(filters)
    
    return (net_info, module_list)


# test the code
blocks = parse_cfg('cfg/yolov3.cfg')
print(create_modules(blocks))


# defining the network
class Darknet(nn.Module):
    def __init__(self, cfgfile):
        super(Darknet, self).__init__()
        self.blocks = parse_cfg(cfgfile)
        self.net_info, self.module_list = create_modules(self.blocks)
        
    # implementing the forward pass
    def forward(self, x, CUDA):
        modules = self.blocks[1:]
        outputs = {}
        write = 0
        for i, module in enumerate(modules):
            module_type = module['type']
            if module_type == 'convolutional' or module_type == 'upsample':
                x = self.module_list[i](x)
            elif module_type == 'route':
                layers = module['layers']
                layers = layers.split(',') # without this, may cause bug
                layers = [int(a) for a in layers]
                
                if layers[0] > 0:
                    layers[0] = layers[0] - i
                    
                if len(layers) == 1:
                    x = outputs[i + layers[0]]                    
                else:
                    if layers[1] > 0:
                        layers[1] = layers[1] - i
                        
                    map1 = outputs[i + layers[0]]
                    map2 = outputs[i + layers[1]]
                    x = torch.cat((map1, map2), 1)
                    
            elif module_type == 'shortcut':
                from_ = int(module['from'])
                x = outputs[i - 1] + outputs[i + from_]
