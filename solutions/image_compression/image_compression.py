from matplotlib.image import imread
import matplotlib.pyplot as plt
import numpy as np

color_image = imread('zoro.jpeg')

plt.imshow(color_image)

color_image.shape

grayscale = np.mean(color_image[:, :, :3], -1)
grayimg = plt.imshow(grayscale)
grayimg.set_cmap('gray')
plt.show()

grayscale.shape

def show_image(image, x_approx, r):
    plt.subplot(1, 2, 1)
    plt.imshow(color_image)
    plt.title('Original')

    plt.subplot(1, 2, 2)
    plt.imshow(x_approx)
    plt.title("Compressed at r="+str(r))

    plt.show()

def compress(image, r):
    U, S, Vt = np.linalg.svd(image, full_matrices=False)
    x_approx = U[:, :r] @ np.diag(S[:r]) @ Vt[:r, :]
    return x_approx

def coloured_compression(image, r):
    red, green, blue = image[:, :, 0], image[:, :, 1], image[:, :, 2]
    com_red = compress(red, r)
    com_green = compress(green, r)
    com_blue = compress(blue, r)
    com_red = com_red/com_red.max()
    com_green = com_green/com_green.max()
    com_blue = com_blue/com_blue.max()
    compressed_image = np.stack([com_red, com_green, com_blue], axis=2)
    return compressed_image

show_image(color_image, coloured_compression(color_image, 1), 1)