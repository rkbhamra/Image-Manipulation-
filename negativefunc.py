import numpy as np
from PIL import Image

class negativefunc:
    def __init__(self, func, img_array: np.array):
        self.func = func
        self.img_array = img_array

    def __call__(self, x):
        return -self.func(x)
    
    def negative_image(img_array):
        for i in range(len(img_array)):
            for j in range(len(img_array[i])):
                for k in range(len(img_array[i][j])):
                    img_array[i][j][k] = 255-img_array[i][j][k]
        return img_array