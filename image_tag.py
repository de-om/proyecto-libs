import os
import sys

from PIL import Image, ImageDraw

image_path = sys.argv[1]
splitted_path = os.path.splitext(image_path)
new_image_path = f"{splitted_path[0]}-stamped{splitted_path[1]}"

im = Image.open(image_path)
width, height = im.size
txt = f"{width} x {height}"
draw = ImageDraw.Draw(im, "RGBA")
_, _, text_width, text_height = draw.textbbox((0, 0), txt)
draw.text((5, height - 5 - text_height), txt, fill="white")

im.save(new_image_path)
