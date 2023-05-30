import sys

from PIL import Image

images = []

## to get the name if the image rather than the file use [1:]
for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)
