'''def average_pixels(img_array):
    if len(img_array.shape) == 3:
        height, width, channels = img_array.shape
        avg_img_array = img_array.mean(axis=2)  
        return avg_img_array
    else:
        return img_array
'''