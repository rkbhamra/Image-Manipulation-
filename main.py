from PIL import Image
import numpy as np 
import matplotlib.pyplot as plt
from negativefunc import negativefunc
from hist_equ import HistogramEqualization

# These are all the available functions that can be applied to the image
def get_input():
    print('''
    1. Negative
    2. Logarithmic
    3. Power Law
    4. Histogram Equalization''')
    choice = input("Enter the function you would like to apply to the image: ")
    if choice == '1':
        negative_image()
    elif choice == '2':
        logarithmic_image()
    elif choice == '3':
        power_law_image()
    elif choice == '4':
        return "histogram_equalization_image()"
    return 1

# print the first image
img = Image.open('img1.png')
img_array = np.array(img)
print(f"Image array shape: {img_array.shape}")
plt.imshow(img_array, cmap='gray') 
 
# This is the function that will be applied to the image
averaged_image = HistogramEqualization.equalize_histogram(img_array)

def show_image(image):
    pixel_plot = plt.figure()
    plt.title("Pixel Plot")
    pixel_plot = plt.imshow(image, cmap='twilight', interpolation='nearest')
    plt.colorbar(pixel_plot)
    plt.savefig('pixel_plot.png')
    plt.show()

show_image(img_array)

