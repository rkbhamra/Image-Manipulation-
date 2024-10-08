import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

class HistogramEqualization:
    def __init__(self, image_path):
        self.image_path = image_path
        if self.image is None:
            raise ValueError("Image not found or unable to load.")
        
    def average_image(image_array):
        if len(image_array.shape) == 3:
            height, width, channels = image_array.shape
            avg_img_array = []
            for i in image_array:
                avg_img_array.append([])
                for j in i:
                    l = 0
                    for k in j:
                        l += k
                    avg_img_array[-1].append(int(l/3))
            return avg_img_array
        else:
            return image_array
        return image_array

    def equalize_histogram(image_array):
        return 1
    
    img = Image.open('img1.png')
    img_array = np.array(img)
    #print(average_image(img_array))
    plt.imshow(average_image(img_array), cmap='gray') 
    plt.show()

