from bluetooth_client import *
from PIL import Image
import numpy


img = Image.open("C:\\Users\\ludwi\\Desktop\\DatenDenker.png")
imgarr = numpy.array(img)
print(img)

#btclient_setup()[0]
#btclient_send(imgarr)

