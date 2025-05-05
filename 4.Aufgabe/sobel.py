import numpy as np
import matplotlib.pyplot as plt
from skimage import io
import time

def rgb_2_gray(img, mode='lut'):
    if mode == 'lut':
        return np.round(img[:,:,0] * 0.2126 + img[:,:,1] * 0.7152 + img[:,:,2] * 0.0722)
    else:
        return np.round(img[:,:,0] * 0.2126 + img[:,:,1] * 0.587 + img[:,:,2] * 0.114)
    

def sobel(img, filter):
    # TODO: implement sobel filtering e.g. with 4 foor loops
    
    filtered_img = np.zeros((gray.shape[0]-2, gray.shape[1]-2))
    return filtered_img


img = io.imread("lena.jpg")
gray = rgb_2_gray(img)

height, width = gray.shape

# define filter in x in y direction
filter_x = np.array([[1, 0, -1],
                       [2, 0, -2],
                       [1, 0, -1]])

filter_y = np.array([[1, 2, 1],
                     [0, 0, 0],
                     [-1, -2, -1]])


start = time.time()
x_img = np.zeros((height-2, width-2))
# TODO: filter image in x direction (sobel(gray, filter_x))
for i in range(0, height-2):
    for j in range(0, width-2):
        for k in range(0, 3):
            for l in range(0, 3):
                x_img[i][j] += gray[i+k][j+l] * filter_x[k][l]
end = time.time()
duration = end-start
print("Duration in milliseconds: ", duration*1000)

start = time.time()
y_img = np.zeros((height-2, width-2))
# TODO: filter image in y direction (sobel(gray, filter_y))
for i in range(0, height-2):
    for j in range(0, width-2):
        for k in range(0, 3):
            for l in range(0, 3):
                y_img[i][j] += gray[i+k][j+l] * filter_y[k][l]
end = time.time()
duration = end-start
print("Duration in milliseconds: ", duration*1000)

#save filtered image
plt.imsave("sobel_x.jpg", x_img, cmap='gray')
plt.imsave("sobel_y.jpg", y_img, cmap='gray')

# TODO compute Gradient magnitude
