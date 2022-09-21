import cv2

img = cv2.imread("jay.png")
img = cv2.resize(img, (128, 128))

for line in img:
    for pixel in line:
        print("{0},{1},{2},".format(pixel[2], pixel[1], pixel[0]))
