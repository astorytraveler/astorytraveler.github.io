# This line imports or includes the library we will need
from PIL import Image

Image_back = Image.open("beach.jpg")
Image_green = Image.open("cat.jpg")
pixels_back = Image_back.load()
pixels_green = Image_green.load()
image_new = Image.new("RGB", Image_back.size)
pixels_new = image_new.load() 
width, height = Image_back.size
for y in range(height):
    for x in range(width):
        (r, g, b) = pixels_green[x,y]
        if r < 100 and g > 100 and b < 100:
            pixels_new[x,y] = pixels_back[x,y]
        else:
            pixels_new[x,y] = pixels_green[x,y]
image_new = image_new.convert("L")
image_new.show()                

image_new.save("the_new_image.jpg")