import cv2

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Left button clicked at ({x}, {y})")
    elif event == cv2.EVENT_RBUTTONDOWN:
        print(f"Right button clicked at ({x}, {y})")

# Create a black image window
image = np.zeros((512, 512, 3), np.uint8)
cv2.imshow("Image", image)

# Set the callback function for mouse events
cv2.setMouseCallback("Image", mouse_callback)

# Wait for a key press and exit
cv2.waitKey(0)
cv2.destroyAllWindows()
