from skimage.io import imread
from skimage.filters import threshold_otsu
import matplotlib.pyplot as plt

car_image = imread('pictures/car1.jpg', as_gray=True)

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.imshow(car_image, cmap='gray')
############## this code creates binary image where compares pixel intensity if it greater than threshold it will be True else will be False
threshold_value = threshold_otsu(car_image)
binary_car_image = car_image > threshold_value
##############
ax2.imshow(binary_car_image, cmap="gray")
# plt.show()
