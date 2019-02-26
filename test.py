import fitz
import os
import numpy as np
from skimage import io
from skimage.color import rgb2gray
from skimage.measure import compare_ssim
from matplotlib import pyplot as plt
from PIL import Image
from PIL import ImageChops
from PIL import ImageDraw
print(fitz.__doc__)

pdfPath = r'C:\ISIS\afpds\amacln5.pdf'
imageName = r'testing'
#savedImgPath = r"E:\pdfCompare\"
#imagePath

def converPDFtoPNG(pdfPath,imagePath,pageNo):
    doc = fitz.open(pdfPath)
    page = doc.loadPage(pageNo)
    pix = page.getPixmap(alpha=False)
    pix.writePNG('%s%d.png'%(imagePath,pageNo))




image1 = 'testing1.png'
image2 = 'testing2.png'

im1 = Image.open(image1)
im2 = Image.open(image2)

print(im1)

difference = ImageChops.difference(im1,im2).getbbox()
print(difference)
draw = ImageDraw.Draw(im2)

draw = ImageDraw.Draw(im2)
draw.rectangle(difference, outline = (0,255,0))
print(help(draw.rectangle))

# #converPDFtoPNG(pdfPath,imageName,0)
# main_image1 = io.imread('testing1.png')
# main_image2 = io.imread('testing2.png')

# print(main_image1.shape)
# print(main_image2.shape)

# io.imshow(main_image1)

# main_image1_gray = rgb2gray(main_image1)
# main_image2_gray = rgb2gray(main_image2)
# io.show()

# print(main_image1_gray.shape)
# print(main_image2_gray.shape)

# io.imshow(main_image1_gray)
# io.show()

# #pix.writeImage(r'E:\pdfCompare\testimg.png',".png")

