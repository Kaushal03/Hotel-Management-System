import cv2 as cv

# Read in an image
img = cv.imread(r'C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\gallery\g912.jpg')
cv.imshow('Park', img)

resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

cv.imwrite(r'C:\Users\Admin\AppData\Local\Programs\Python\Python310\My Programs\Hotel Management System\gallery/g11.jpg',resized)

cv.waitKey(0)
