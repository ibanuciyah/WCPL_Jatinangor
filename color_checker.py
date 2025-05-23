import cv2

def get_pixel_color(event, x, y, flags, param):
    """Callback function to get RGB color of clicked pixel."""
    if event == cv2.EVENT_LBUTTONDOWN:  # Left mouse button click
        img = param  # Retrieve image from param
        b, g, r = img[y, x]  # OpenCV stores images in BGR format
        print(f"RGB color at ({x}, {y}): ({r}, {g}, {b})")
        return (r, g, b)  # Return RGB values

# Load image
image_path = 'hasil.png'  # Change to your image file path
img = cv2.imread(image_path)

if img is None:
    raise FileNotFoundError(f"Image not found: {image_path}")

# Create window and set mouse callback
cv2.imshow("Click on Pixel", img)
cv2.setMouseCallback("Click on Pixel", get_pixel_color, img)

# Wait until a key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()