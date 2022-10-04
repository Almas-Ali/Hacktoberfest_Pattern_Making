from PIL import Image
import os


def main():
    # path of the folder containing the raw images
    inPath = ""

    # path of the folder that will contain the modified image
    outPath = ""

    for imagePath in os.listdir(inPath):
        # imagePath contains name of the image
        inputPath = os.path.join(inPath, imagePath)

        # inputPath contains the full directory name
        img = Image.open(inputPath)

        fullOutPath = os.path.join(outPath, imagePath +'.png')
        # fullOutPath contains the path of the output
        # image that needs to be generated
        print(fullOutPath)

# Driver Function
if __name__ == '__main__':
    main()