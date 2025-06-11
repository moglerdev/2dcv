import numpy as np
import matplotlib.pyplot as plt
from skimage import io
import time
import sobel_demo as nd
from sobel import rgb_2_gray

img = io.imread("lena.jpg")
gray = rgb_2_gray(img).astype("float64")

# Define Sobel filters
filter_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
filter_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])


start = time.time()
# Filter image in x direction
filtered_x = nd.sobel(gray, filter_x)
end = time.time()
duration = end-start
print("Duration C++ (x-direction) in milliseconds: ", duration*1000)


start = time.time()
# Filter image in y direction
filtered_y = nd.sobel(gray, filter_y)
end = time.time()
duration = end-start
print("Duration C++ (y-direction) in milliseconds: ", duration*1000)

# Compute Gradient magnitude
gradient_magnitude = np.sqrt(filtered_x**2 + filtered_y**2)

# Normalize magnitude for display
#gradient_magnitude = (gradient_magnitude / np.max(gradient_magnitude) * 255).astype(np.uint8)

# Display the results
plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1)
plt.imshow(gray, cmap='gray')
plt.title('Original')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(gradient_magnitude, cmap='gray')
plt.title('Sobel Gradient Magnitude (C++)')
plt.axis('off')

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(np.abs(filtered_x), cmap='gray')
plt.title('Sobel X Gradient (C++)')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(np.abs(filtered_y), cmap='gray')
plt.title('Sobel Y Gradient (C++)')
plt.axis('off')


plt.show()