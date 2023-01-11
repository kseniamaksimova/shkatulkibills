from PIL import Image
def bilde():
 datne = "bilde.jpg"
 with Image.open(datne) as im:
  print(datne, im.format, f"{im.size}x{im.mode}")
  im.show()
  izmers = (500, 500)
  im_rotate = im.rotate(90, expand=True)
  im_rotate.save('bilde-maza-90.jpg', quality=95)
  im.thumbnail(izmers)
  im.save("bilde-maza.jpg", im.format)
  im.show()
bilde()