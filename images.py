from PIL import Image,ImageFilter

img=Image.open("./Pokedex/pikachu.jpg")

filitered_image=img.filter(ImageFilter.BLUR)
filitered_image.save('blurred.png','png')