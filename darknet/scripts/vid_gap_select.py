import sys
from utils import gap_select

if __name__ == '__main__':
    det_dir, vid_dir = sys.argv[1:3]
    gap_select(vid_dir, det_dir)