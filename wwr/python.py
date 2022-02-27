# This line imports or includes the library we will need
from PIL import Image

# This line opens the image and loads it into a variable called "image_original"
image_original = Image.open("beach.jpg")


width, height = image_original.size

pixels_original = image_original.load()

r, g, b = pixels_original[100, 200]

pixels_original[100, 200] = (255, 0, 255)

# This line attempts to open a new window to display the image.
image_original.show()

