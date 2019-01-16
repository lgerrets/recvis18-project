import os
import math
import re
from argparse import ArgumentParser
from collections import OrderedDict

from PIL import Image
import numpy as np
import scipy.misc


def build_parser():
    parser = ArgumentParser()
    parser.add_argument('--target',
            dest='target', help='target image',
            metavar='TARGET', required=True)
    parser.add_argument('--pred',
            dest='pred', help='predicted image',
            metavar='PRED', required=True)
    return parser

def imread(path):
    img = scipy.misc.imread(path).astype(np.float)
    if len(img.shape) == 2:
        # grayscale
        img = np.dstack((img,img,img))
    elif img.shape[2] == 4:
        # PNG with alpha channel
        img = img[:,:,:3]
    return img

def main():
    parser = build_parser()
    options = parser.parse_args()

    target_image = imread(options.target)/255
    pred_image = imread(options.pred)/255

    assert target_image.shape == pred_image.shape

    loss = ((target_image - pred_image)**2).sum()/(np.prod(target_image.shape))
    loss = np.sqrt(loss) # in [0,1]

    print("Loss",loss)


if __name__ == '__main__':
    main()

