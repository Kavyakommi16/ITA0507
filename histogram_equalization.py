import cv2

image = cv2.imread("sample.png")

if image is None:
    print("Error: Image not found!")
    exit()

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
equalized_image = cv2.equalizeHist(gray_image)

cv2.imshow("Original Grayscale Image", gray_image)
cv2.imshow("Histogram Equalized Image", equalized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
