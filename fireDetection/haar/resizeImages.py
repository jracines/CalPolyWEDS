import cv2 as cv
import glob

def main():
    # Read only .jpg files 
    filenames = glob.glob("positive/*.jpg")
    filenames.sort()
    images = [cv.imread(img) for img in filenames]

    # Resize each image to this width and height

    # Resize each image 
    for img in images:
        print(img.shape)


if __name__ == "__main__":
    main()