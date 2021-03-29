import cv2 as cv
import glob

def main():
    # Read only .jpg files 
    filenames = glob.glob("positive/*.jpg")
    filenames.sort()
    images = [cv.imread(img) for img in filenames]

    # Scaling dimensions

    # Resize each image 
    for img in images:
        print(img)


if __name__ == "__main__":
    main()