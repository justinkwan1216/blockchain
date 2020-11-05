import cv2
from PIL import Image
import numpy as np
# Load the image and convert to 32-bit RGBA
img = np.array(Image.open("python.jpg")).astype('uint8')

#img = cv2.imread(img, cv2.IMREAD_UNCHANGED)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print('Original Dimensions : ',img.shape)
 
scale_percent = 60       # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (24,24)
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
cv2.imwrite('output.jpg',resized)
 
