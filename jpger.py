import os
import cv2

for (root, dirs, files) in os.walk("github"):
    for filename in files:
        name = os.path.join(root,filename)
        if name[-4:] == '.png':
            print(name)
            img = cv2.imread(name)
            cv2.imwrite(name[:-4] + '.jpg', img)
