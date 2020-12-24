from PIL import Image, ImageOps

images = ["1.png", "2.png", "3.png", "4.png", "5.png", "6.png", "7.png", "8.png"]


for i in images:
    image = Image.open(i)
    
    imageResized = image.resize((50, 50))
    

    imageResized.save("resized/" + i, "PNG")
