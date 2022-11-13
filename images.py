from PIL import Image, ImageFilter

img = Image.open("./Pokedex/pikachu.jpg")

filitered_image = img.filter(ImageFilter.BLUR)
filitered_image.save('blurred.png', 'png')

filitered_image2 = img.filter(ImageFilter.SMOOTH)
filitered_image2.save('smooth.png', 'png')

filitered_image3 = img.filter(ImageFilter.SHARPEN)
filitered_image3.save('sharpen.png', 'png')

filitered_image4 = img.convert('L')
filitered_image4.save('grey.png', 'png')

filitered_image5 = img.rotate(90)
filitered_image5.save('rotated.png', 'png')


