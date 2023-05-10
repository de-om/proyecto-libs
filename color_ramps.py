from itertools import product

import numpy as np
from PIL import Image

width, height = 256, 256
im = Image.new("RGB", (width, height))
pix_matrix = np.array(im)
for x, y in product(range(width), range(height)):
    pix_matrix[x, y] = (x, y, (x + y) // 2)
im = Image.fromarray(pix_matrix)
im.show()
