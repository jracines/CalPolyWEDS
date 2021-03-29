import cv2 as cv
import glob

def main():
    # Read only .jpg files 
    pos_filenames = glob.glob("positive/*.jpg")
    neg_filenames = glob.glob("negative/*.jpg")
    pos_filenames.sort()
    neg_filenames.sort()
    pos_images = [cv.imread(img) for img in pos_filenames]
    neg_images = [cv.imread(img) for img in neg_filenames]

    # Resize each image to this width and height
    width = 1200
    height = 800
    dim = (width, height)

    # Resize each image 
    # for img in pos_images:
    for img_file in pos_filenames:
        img = cv.imread(img_file)
        img = cv.resize(img, dim, interpolation = cv.INTER_AREA)
        cv.imwrite(img_file, img)
    # for img in neg_images:
    for img_file in neg_filenames:
        img = cv.imread(img_file)
        img = cv.resize(img, dim, interpolation = cv.INTER_AREA)
        cv.imwrite(img_file, img)

if __name__ == "__main__":
    main()