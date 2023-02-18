from PIL import Image
img = Image.open('lenna.png')
print(img.size)
print(img.format)
img.show()

area = (100,100,320,320)
cropImage = img.crop(area)
img.show()
cropImage.show()

size = (64, 64)
img.thumbnail(size)
img.save('lenna-thumb.png')
img.show()
img = Image.open('lenna.png')
img2 = img.resize((300,300))
img2.save('lenna_300.png')
img2.show()

img = Image.open('lenna.png')
img3 = img.rotate(90)
img3.save('lenna_rotate.png')
img3.show()

img = Image.open('lenna.png')
mirrorImage = img.transpose(Image.FLIP_LEFT_RIGHT)
mirrorImage.save('lenna-mirror.png')
mirrorImage.show()

updownImage = img.transpose(Image.FLIP_TOP_BOTTOM)
updownImage.save('lenna-updown.png')


from PIL import Image, ImageFilter
img = Image.open('lenna.png')
contourImage = img.filter(ImageFilter.CONTOUR)
contourImage.save('lenna-contour.png')
contourImage.show()
blurImage = img.filter(ImageFilter.BLUR)
blurImage.save('lenna-blur.png')
blurImage.show()
embossImage = img.filter(ImageFilter.EMBOSS)
embossImage.save('lenna-emboss.png')
embossImage.show()



from PIL import Image
new_york = Image.open('newyork.jpg')
print(new_york.mode)
# 이미지의 R, G, B를 분리함
r, g, b = new_york.split()
r.save('newyork_r.jpg')
r.show()
g.save('newyork_g.jpg')
g.show()
b.save('newyork_b.jpg')
b.show()