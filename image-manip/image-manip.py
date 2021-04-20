from PIL import Image

#open the image 
myImg = Image.open("hh.jpg")


#showing the image
myImg.show()


#cropping
box = (50,50,200,200)

newImg = myImg.crop(box)

myImg.show()
newImg.show()
