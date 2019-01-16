import os
from os.path import isfile, join
import math
import re
from argparse import ArgumentParser
from collections import OrderedDict

from PIL import Image
import numpy as np
import scipy.misc


def build_parser():
    parser = ArgumentParser()
    parser.add_argument('--images',
            dest='images', help='path to directory of images to be resized',
            metavar='IMAGES', required=True)
    parser.add_argument('--outputs',
            dest='outputs', help='path to directory of outputs',
            metavar='OUTPUTS', required=True)
    parser.add_argument('--width',
            dest='width', help='new width',
            default=400, type=int,
            metavar='WIDTH', required=False)
    parser.add_argument('--height',
            dest='height', help='new height',
            default=600, type=int,
            metavar='HEIGHT', required=False)
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

def imsave(path, img):
    img = np.clip(img, 0, 255).astype(np.uint8)
    Image.fromarray(img).save(path, quality=95)

def main():
    parser = build_parser()
    options = parser.parse_args()

    images_names = [f for f in os.listdir(options.images) if isfile(join(options.images,f))]
    images = [imread(join(options.images,name)) for name in images_names]
    images = [scipy.misc.imresize(img, (options.width,options.height)) for img in images]

    for name,img in zip(images_names,images):
        imsave(join(options.outputs,name),img)


if __name__ == '__main__':
    main()

