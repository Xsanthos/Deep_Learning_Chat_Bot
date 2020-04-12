import time
from Functions import *
import matplotlib.pyplot as plt


def VideoAnalyser():
    videoTake()


def ImageAnalyser():
    print("############## Spectral Analyser ##############\n Welcome!\n")
    time.sleep(0.1)
    print("Would you like to scan a sample for analysis?")
    time.sleep(1)
    choice = input("Yes/No ------ ")
    if choice == "Yes":
        t = "Yes"
        while t == "Yes":
            imageTake(1)
            imageTake(2)
            NDVI(1)
            time.sleep(1)
            file_name = input("Please rename sample file ---")
            renameFile(file_name)
            plt.close()
            time.sleep(1)
            t = input("Would you like to scan another sample? (Yes/No) ---- ")
            if t == "No":
                choice = "No"

    if choice == "No":
        plt.close()
        time.sleep(1)
        print("Thank you for using the app!")


def main():
    thermalIR()


main()
