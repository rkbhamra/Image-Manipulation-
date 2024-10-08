from PIL import Image
import numpy as np 
import matplotlib.pyplot as plt

img = Image.open('img1.png')
img_array = np.array(img)
plt.imshow(img_array, cmap='gray')  

print(f"Image array shape: {img_array.shape}")

'''def average_pixels(img_array):
    if len(img_array.shape) == 3:
        height, width, channels = img_array.shape
        avg_img_array = img_array.mean(axis=2)  
        return avg_img_array
    else:
        return img_array
'''
    
def average_pixels(img_array2):
    img_array3 = img_array2
    for i in range(len(img_array3)):
        for j in range(len(img_array3[i])):
            for k in range(len(img_array3[i][j])):
                img_array[i][j][k] = 255-img_array3[i][j][k]
    return img_array3

averaged_image = average_pixels(img_array)



pixel_plot = plt.figure()

plt.title("Pixel Plot")
pixel_plot = plt.imshow(averaged_image, cmap='twilight', interpolation='nearest')

plt.colorbar(pixel_plot)

plt.savefig('pixel_plot.png')

plt.show()
