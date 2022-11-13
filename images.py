from PIL import Image, ImageFilter

img = Image.open("./Pokedex/pikachu.jpg")

blurred_image = img.filter(ImageFilter.BLUR)
blurred_image.save('blurred.png', 'png')

smooth_image = img.filter(ImageFilter.SMOOTH)
smooth_image.save('smooth.png', 'png')

sharpen_image = img.filter(ImageFilter.SHARPEN)
sharpen_image.save('sharpen.png', 'png')

grey_image = img.convert('L')
grey_image.save('grey.png', 'png')

rotate_image = img.rotate(90)
rotate_image.save('rotated.png', 'png')

resize_image = img.resize((300,300))
resize_image.save('resized.png', 'png')

