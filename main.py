from PIL import Image
import numpy as np 
import matplotlib.pyplot as plt

img = Image.open('img1.png')
# Convert image to numpy array
img_array = np.array(img)

# Print the numpy array
print(img_array)

# Display the image as a pixel value image
plt.imshow(img_array, cmap='gray')
plt.colorbar()
plt.show()