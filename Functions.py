import cv2
import os
import imageio
import numpy as np
import PIL.Image as Image


def imageTake(i):
    path = "./Images"
    camera = cv2.VideoCapture(i)
    camera.set(3, 640)
    camera.set(4, 480)
    return_value, image = camera.read()
    if i < 2:
        cropped = image[78:332, 140:500]
        resize = cv2.resize(cropped, (640, 480))
        cv2.imwrite(os.path.join(path, 'sample' + str(i) + '.png'), resize)
    else:
        cv2.imwrite(os.path.join(path, 'sample' + str(i) + '.png'), image)
    del camera


def videoTake():
    import matplotlib.pyplot as plt

    cam1 = cv2.VideoCapture(1)
    cam1.set(3, 640)
    cam1.set(4, 480)
    cam2 = cv2.VideoCapture(2)
    while (True):
        ret, frame1 = cam1.read()
        cropped = frame1[78:332, 140:500]
        resize = cv2.resize(cropped, (640, 480))
        R = resize[:, :, 1]
        ret2, frame2 = cam2.read()
        IR = frame2[:, :, 0]

        frame = (IR - R) / (IR + R)
        ndvi = (frame + 1) / 2

        cv2.imshow('NDVI', ndvi)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam1.release()
    cam2.release()
    cv2.destroyAllWindows()


def renameFile(name):
    os.rename(r'NDVI\ndvi.png', r'./NDVI\\' + name + '.png')


def thermalIR():
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    imageTake(2)

    im = mpimg.imread('./Images/sample2.png')
    R = im[:, :, 0]

    plt.figure(figsize=(15, 15))
    plt.title("Thermal")
    thermal = plt.imshow(R, cmap="inferno")
    plt.colorbar()
    plt.show(thermal)
    plt.imsave('./Thermal/thermal.png', R)


def rgbSplitter(i):  # Plots separate R G B colored maps
    import imageio
    import matplotlib.pyplot as plt
    pic = imageio.imread('./Images/sample' + str(i) + '.png')

    plt.figure(figsize=(15, 15))
    fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))

    for c, ax in zip(range(3), ax):
        split_img = np.zeros(pic.shape, dtype="uint8")
        split_img[:, :, c] = pic[:, :, c]
        image = ax.imshow(split_img)

    plt.show(image)


def RedChannelSplitter(i):  # Plots R channel
    import matplotlib.pyplot as plt
    pic = imageio.imread('./Images/sample' + str(i) + '.jpg')
    plt.figure(figsize=(15, 15))
    plt.title('R channel')
    plt.ylabel('Height {}'.format(pic.shape[0]))
    plt.xlabel('Width {}'.format(pic.shape[1]))

    plt.imshow(pic[:, :, 0])
    plt.show()


def GreenChannelSplitter(i):  # Plots G channel
    import matplotlib.pyplot as plt
    pic = imageio.imread('./Images/sample' + str(i) + '.jpg')
    plt.figure(figsize=(15, 15))
    plt.title('G channel')
    plt.ylabel('Height {}'.format(pic.shape[0]))
    plt.xlabel('Width {}'.format(pic.shape[1]))

    plt.imshow(pic[:, :, 1])
    plt.show()


def BlueChannelSplitter(i):  # Plots B channel
    import matplotlib.pyplot as plt
    pic = imageio.imread('./Images/sample' + str(i) + '.jpg')
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


def NDVI(i):  # Calculates and plots NDVI
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg

    img1 = mpimg.imread('./Images/sample' + str(i) + '.png')
    R = img1[:, :, 0]
    img2 = mpimg.imread('./Images/sample2.png')
    IR = img2[:, :, 0]

    plt.figure(figsize=(15, 15))
    plt.title("NDVI")
    ndvi = (IR - R) / (IR + R)
    ndvi_array = (ndvi + 1) / 2
    ndvi_plot = plt.imshow(ndvi_array, cmap="summer")

    plt.show(ndvi_plot)
    plt.imsave('./NDVI/ndvi.png', ndvi_array, cmap="summer")


def NDWI(i):  # Calculates and plots NDWI
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg

    img1 = mpimg.imread('./Images/sample' + str(i) + '.png')
    G = img1[:, :, 1]
    img2 = mpimg.imread('./Images/sample2.png')
    IR = img2[:, :, 0]

    plt.figure(figsize=(15, 15))
    plt.title("NDWI")
    ndwi = (G - IR) / (G + IR)
    ndwi_plot = plt.imshow(ndwi, cmap="tab20c")
    plt.colorbar(orientation="horizontal")
    plt.show(ndwi_plot)
    plt.savefig('./NDWI/ndwi.png')
    plt.imsave('./NDWI/ndwi.png', ndwi, cmap="gray")
