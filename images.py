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

resize_image = img.resize((220, 220))
resize_image.save('resized.png', 'png')

cr0p_dimension = (150, 150, 350, 350)
cr0ped_image = img.crop(cr0p_dimension)
cr0ped_image.save('cr0ped.png', 'png')

img2 = Image.open('./j.jpg')
resize_image2 = img2.resize((400, 200))
resize_image2.save('j_resized.png', 'png')

img2.thumbnail((400, 200))
img2.save('jthumb.png', 'png')
