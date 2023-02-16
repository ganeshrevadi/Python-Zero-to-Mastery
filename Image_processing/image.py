from PIL import Image ,ImageFilter

img = Image.open('./Image_processing/pikachu.jpg')
filter_image = img.convert('L')
box = (100,100,400,400)
region = filter_image.crop(box)
region.save("greay.png",'png')
region.show()

