from PIL import Image
import sys
import os

path  =sys.argv[1]
dire = sys.argv[2]

print(path,dire)
loc = os.path.exists(dire)


if not os.path.exists(dire):
    os.mkdir(dire)
else:
    pass    

for img in os.listdir(path):
    clean_name = os.path.splitext(img)[0]
    img = Image.open(f'{path}{img}')
  #added the / in case user doesn't enter it. You may want to check for this and add or remover it. 
    img.save(f'{dire}/{clean_name}.png', 'png')
    print('all done!')
 
