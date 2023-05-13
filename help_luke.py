from PIL import Image, ImageDraw, ImageFilter

im = Image.open("luke.png")
width, height = im.size
vfx = Image.new("RGBA", (width, height))
canvas = ImageDraw.Draw(vfx)
line_coord = ((380, 498), (-35, 34))
canvas.line(line_coord, fill="#00FF00", width=24)
for _ in range(18):
    vfx = vfx.filter(ImageFilter.BLUR)
canvas = ImageDraw.Draw(vfx)
canvas.line(line_coord, fill="#FFFFFF", width=18)
vfx = vfx.filter(ImageFilter.BLUR)
im.alpha_composite(vfx, (0, 0))
im.save("luke-vfx.png")
