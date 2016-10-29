from __future__ import division, print_function, absolute_import

import numpy as np

from scipy import misc
from scipy import ndimage as nd


img = misc.imread('projective_challenge/pics/0_0.jpg')
img = img.astype('int32')
dx = nd.sobel(img, 0)
dy = nd.sobel(img, 1)
magnitude = np.hypot(dx, dy)
# magnitude *= 255.0 / np.max(magnitude)
misc.imsave('sobel.jpg', magnitude)
