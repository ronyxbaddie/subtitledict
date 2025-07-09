from PIL import ImageGrab

# Define a test region (example: subtitles area)
bbox = (600, 700, 1300, 750)  # (x1, y1, x2, y2)

# Capture that area
screenshot = ImageGrab.grab(bbox)

# Show the captured image
screenshot.show()
