import cv2

# Read the image
image = cv2.imread("sample.png")

# Check if the image is loaded successfully
if image is None:
    print("Error: Image not found. Check the file name and path.")
else:
    # Apply Gaussian Blur
    blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

    # Display the images
    cv2.imshow("Original Image", image)
    cv2.imshow("Blurred Image", blurred_image)

    # Wait until a key is pressed
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
