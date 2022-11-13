from PIL import Image, ImageFilter

img = Image.open("./Pokedex/pikachu.jpg")

filitered_image = img.filter(ImageFilter.BLUR)
filitered_image.save('blurred.png', 'png')

filitered_image2 = img.filter(ImageFilter.SMOOTH)
filitered_image2.save('smooth.png', 'png')
