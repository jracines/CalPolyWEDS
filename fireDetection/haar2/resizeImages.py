import cv2 as cv

def main():
    filenames = glob.glob("positive/*.jpg")
    filenames.sort()
    images = [cv.imread(img) for img in filenames]

    for img in images:
        print(img)


if __name__ == "__main__":
    main()