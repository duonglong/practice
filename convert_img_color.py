from PIL import Image
import numpy as np
# FILE_NAME = "L_2d_cropped.png"
FILE_NAME = "moderate_forest.8598.png"
im = Image.open(FILE_NAME)
im.convert('RGBA')
pixels = im.load()
for y in range(im.size[1]):
        for x in range(im.size[0]):
            r, g, b, a = pixels[x, y]
            if (r, g, b, a) != (0, 0, 0, 0):
                print pixels[x, y]
            if a != 255:
                r = r * a // 255
                g = g * a // 255
                b = b * a // 255
                pixels[x, y] = (r, g, b, a)


a = 1
# FILE_NAME = "moderate_forest.8598.png"

# picture = Image.open(FILE_NAME)
#
# width, height = picture.size
#
# yellow = (255,255,0)
#
# for x in range(0, width):
#     for y in range(0, height):
#         picture.putpixel( (x,y), yellow)
# picture.show()

# import numpy as np
# from PIL import Image
#
# im = Image.open(FILE_NAME)
# data = np.array(im)
# im.convert('RGBA')
# r1, g1, b1 = 0, 0, 0 # Original value
# r2, g2, b2 = 255, 255, 0 # Value that we want to replace it with
#
# red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
# mask = (red == r1) & (green == g1) & (blue == b1)
# data[:,:,:3][mask] = [r2, g2, b2]

# im = Image.fromarray(data)
# im.save('fig1_modified.png')
# im.show()