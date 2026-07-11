import cv2

# Read the image
image = cv2.imread("sample.png")

# Check if image is loaded
if image is None:
    print("Error: Image not found.")
else:
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny Edge Detection
    edges = cv2.Canny(gray_image, 100, 200)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Edge Detected Image", edges)

    # Wait for key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
