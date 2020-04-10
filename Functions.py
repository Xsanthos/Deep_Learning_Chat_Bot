import cv2
import os
import imageio
import numpy as np


def imageTake():
    path = "./Images"
    camera = cv2.VideoCapture(0)
    return_value, image = camera.read()
    cv2.imwrite(os.path.join(path, 'sample' + '.jpg'), image)
    del camera


def RenameFile(name):
    os.rename(r'./Images\spectrum.png', r'./Images\\' + name + '.png')
    os.rename(r'./BMP\spectrum1.png', r'./BMP\\' + name + '.bmp')


def rgbSplitter():  # Plots separate R G B colored maps
    import imageio
    import matplotlib.pyplot as plt
    pic = imageio.imread('./Images/sample.jpg')

    plt.figure(figsize=(15, 15))
    fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))

    for c, ax in zip(range(3), ax):
        split_img = np.zeros(pic.shape, dtype="uint8")
        split_img[:, :, c] = pic[:, :, c]
        image = ax.imshow(split_img)

    plt.show(image)


def RedChannelSplitter():  # Plots R channel
    import matplotlib.pyplot as plt
    pic = imageio.imread('./Images/sample.jpg')
    plt.figure(figsize=(15, 15))
    plt.title('R channel')
    plt.ylabel('Height {}'.format(pic.shape[0]))
    plt.xlabel('Width {}'.format(pic.shape[1]))

    plt.imshow(pic[:, :, 0])
    plt.show()


def GreenChannelSplitter():  # Plots G channel
    import matplotlib.pyplot as plt
    pic = imageio.imread('./Images/sample.jpg')
    plt.figure(figsize=(15, 15))
    plt.title('G channel')
    plt.ylabel('Height {}'.format(pic.shape[0]))
    plt.xlabel('Width {}'.format(pic.shape[1]))

    plt.imshow(pic[:, :, 1])
    plt.show()


def BlueChannelSplitter():  # Plots B channel
    import matplotlib.pyplot as plt
    pic = imageio.imread('./Images/sample.jpg')
    plt.figure(figsize=(15, 15))
    plt.title('B channel')
    plt.ylabel('Height {}'.format(pic.shape[0]))
    plt.xlabel('Width {}'.format(pic.shape[1]))

    plt.imshow(pic[:, :, 0])
    plt.show()


'''def RGBtoWavelength(r, g, b):  ## May not be used!
    with open('wavelengths.json') as data:
        for item in data["wave_lengths"]:
            color = item["color"]
            if color[0] == r and color[1] == g and color[2] == b:
                return int(item["wavelength"])'''


def NDVI():  # Calculates and plots NDVI
    import matplotlib.pyplot as plt

    im = cv2.imread('./Images/sample.jpg').astype(np.float)
    B, G, R = cv2.split(im)

    ndvi = (G - R) / (G + R + 0.0001)
    ndviplot = plt.imshow(ndvi)
    plt.show(ndviplot)
    plt.savefig('./Images/NDVI/ndvi.jpg')

