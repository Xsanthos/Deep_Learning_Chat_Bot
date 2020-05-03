import os
import numpy as np
import time


def renameFile(name, location):
    os.rename(r'./NDVI\ndvi.png', r'./' + location + '\\' + name + '.png')


def thermalIR():
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg

    im = mpimg.imread('./Images/NIR.png')
    IR = im[:, :, 0]

    plt.figure(figsize=(15, 15))
    plt.title("Thermal")
    thermal = plt.imshow(IR, cmap="inferno")
    plt.colorbar()
    plt.show(thermal)
    plt.imsave('./Thermal/thermal.png', IR)


def rgbSplitter(i):  # Plots separate R G B colored maps
    import imageio
    import matplotlib.pyplot as plt
    pic = imageio.imread('./Images/' + str(i) + '.jpg')

    plt.figure(figsize=(15, 15))
    fig, ax = plt.subplots(nrows=1, ncols=7, figsize=(15, 5))

    for c, ax in zip(range(3), ax):
        split_img = np.zeros(pic.shape, dtype="uint8")
        split_img[:, :, c] = pic[:, :, c]
        image = ax.imshow(split_img)

    plt.show(image)


'''def RGBtoWavelength(r, g, b):  ## May not be used!
    with open('wavelengths.json') as data:
        for item in data["wave_lengths"]:
            color = item["color"]
            if color[0] == r and color[1] == g and color[2] == b:
                return int(item["wavelength"])'''


def NDVI():  # Calculates and plots NDVI
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg

    img1 = mpimg.imread('./Images/RGB.png')
    img2 = mpimg.imread('./Images/NIR.png')
    R = img1[:, :, 2]
    IR = img2[:, :, 2]

    plt.figure(figsize=(15, 15))
    plt.title("NDVI")
    ndvi = (IR - R) / (IR + R + 0.0001)
    ndvi_array = (ndvi + 1) / 2
    ndvi_plot = plt.imshow(ndvi_array, cmap="summer")
    plt.show(ndvi_plot)
    plt.imsave('./NDVI/ndvi.png', ndvi_array, cmap="summer")


# Calculates and plots NDWI
def NDWI():
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg

    img1 = mpimg.imread('./Images/RGB.png')
    img2 = mpimg.imread('./Images/NIR.png')
    G = img1[:, :, 1]
    IR = img2[:, :, 2]

    plt.figure(figsize=(15, 15))
    plt.title("NDWI")
    ndwi = (G - IR) / (G + IR + 0.0001)
    ndwi_plot = plt.imshow(ndwi, cmap="tab20c")
    plt.show(ndwi_plot)
    plt.imsave('./NDWI/ndwi.png', ndwi, cmap="tab20c")