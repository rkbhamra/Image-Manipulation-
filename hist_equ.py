import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

class HistogramEqualization:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = Image.open(image_path)  
        if self.image is None:
            raise ValueError("Image not found or unable to load.")
        
    def average_image(self, image_array):
        """Convert an RGB image to grayscale by averaging the RGB channels."""
        if len(image_array.shape) == 3: 
            avg_img_array = []
            for i in image_array:
                avg_img_array.append([])
                for j in i:
                    avg_pixel_value = np.uint16(0)
                    for k in j:
                        avg_pixel_value += k
                    avg_img_array[-1].append(np.uint8(avg_pixel_value / 3)) 
            return np.array(avg_img_array)
        else:
            return image_array 
    
    def count_pixels(self, image_array):
        """Count occurrences of each pixel value (0-255) in the image."""
        count_list = [0] * 256
        height, width = image_array.shape
        for i in range(height):
            for j in range(width):
                pixel_value = image_array[i][j]
                count_list[pixel_value] += 1
        return count_list
    
    def calc_probability(self, pixel_count_array):
        """Calculate the probability of each pixel intensity."""
        total_pixels = sum(pixel_count_array)
        prob_list = [count / total_pixels for count in pixel_count_array]
        return prob_list

    def equalize_histogram(self):
        """Equalize the pixel intensities of the image."""
        img_array = np.array(self.image)
        avg_img_array = self.average_image(img_array)  
        pixel_counts = self.count_pixels(avg_img_array)  
        probabilities = self.calc_probability(pixel_counts)  

        s = []
        s.append(((len(probabilities)-1) * probabilities[0]))
        for i in range(1, len(probabilities)):
            s.append((((len(probabilities)-1) * probabilities[i]) + s[i-1]))
        print("S",s)

        for i in range(avg_img_array.shape[0]):
            for j in range(avg_img_array.shape[1]):
                avg_img_array[i][j] = round(s[int(avg_img_array[i][j])])#, 0, 255)
        return avg_img_array

    def apply_equalization(self):
        """Equalize and display histogram of pixel intensities."""
        img_array = np.array(self.image)
        avg_img_array = self.average_image(img_array)  
        equalized_image = self.equalize_histogram()  

        #plot the original and equalized images
        fig, ax = plt.subplots(1, 2, figsize=(12, 6))
        ax[0].imshow(avg_img_array, cmap='gray')
        ax[0].set_title("Original Image")
        ax[1].imshow(equalized_image, cmap='gray')
        ax[1].set_title("Equalized Image")
        plt.show()

# Example usage
image_path = 'img1.png'  
hist_eq = HistogramEqualization(image_path) 
hist_eq.apply_equalization()  
