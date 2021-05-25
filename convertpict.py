from PIL import Image

imageFile = input()
format = input()
format = list(format.split(" "))

try:  
  image=Image.open(imageFile)
  image=image.crop((0,0,formaz[0],format[1]))
  image=image.convert('RGBA')
  image.save(imageFile)
  print("Image was saved to: "+imageFile+", in "+format[0]+"x"+format[1]+" format.")
except:
  print("There was an error. Did you run with sudo?")