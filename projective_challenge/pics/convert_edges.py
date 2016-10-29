from __future__ import division
import os

import cv2
import numpy as np
from scipy import misc


def auto_canny(img, sigma=0.33):
    med = np.median(img)

    low = int(max(0, (1.0 - sigma) * med))
    high = int(min(255, (1.0 + sigma) * med))

    edges = cv2.Canny(img, low, high)

    return edges


def convert_edges(f_name):
    img = misc.imread(f_name)
    img = cv2.GaussianBlur(img, (5, 5), 0)
    img = auto_canny(img)

    misc.imsave('edges/' + f_name, img)


if __name__ == '__main__':
    for f_name in os.listdir('.'):
        if f_name.endswith('.jpg') and os.path.isfile(f_name):
            convert_edges(f_name)
