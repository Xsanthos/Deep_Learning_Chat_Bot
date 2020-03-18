from Functions import *
import os

choice = input("Would you like to scan the sample? y/n")
if choice == "y":
    imageTake()
    changeN = input("Please rename file")
    os.rename(r'./Images\spectrum.png', r'./Images\\'+changeN+'.png')
    os.rename(r'./BMP\spectrum1.png', r'./BMP\\' + changeN + '.bmp')

