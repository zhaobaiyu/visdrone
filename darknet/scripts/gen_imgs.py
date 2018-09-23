import sys
from utils import gen_more_imgs, gen_images_txt


if __name__ == '__main__':
    src_dir, dst_dir = sys.argv[1:3]
    gen_more_imgs(src_dir, dst_dir)
    gen_images_txt(dst_dir)