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
from skimage.filters import threshold_otsu
from skimage.measure import find_contours
from skimage.color import gray2rgb
print(fitz.__doc__)

pdfPath = r'C:\ISIS\afpds\amacln5.pdf'
imageName = r'testing'
#savedImgPath = r"E:\pdfCompare\"
#imagePath

def converPDFtoPNG(pdfPath,imagePath,pageNo):
    doc = fitz.open(pdfPath)
    page = doc.loadPage(pageNo)
    pix = page.getPixmap(alpha=False)
    img = Image.frombuffer("RGB", [pix.width, pix.height], pix.samples,"raw", "RGB", 0, 1)
    img.save("testing%d.jpeg"%pageNo)


    #pix.writeImage('%s%d.jpg'%(imagePath,pageNo))
#converPDFtoPNG(pdfPath,imageName,0)

def drawShape(img,coordinates,color):
    #img = gray2rgb(img)
    print(img.shape)
    coordinates = coordinates.astype(int)

    img[coordinates[:, 0],coordinates[:, 1]] = color

    return img


# image1 = 'testing1.png'
# image2 = 'testing2.png'

# im1 = Image.open(image1)
# im2 = Image.open(image2)

# print(im1)

# difference = ImageChops.difference(im1,im2).getbbox()
# print(difference)
# draw = ImageDraw.Draw(im2)

# draw = ImageDraw.Draw(im2)
# draw.rectangle(difference, outline = (0,255,0))
# print(help(draw.rectangle))

#converPDFtoPNG(pdfPath,imageName,0)



def find_difference_in_image(image1_path,image2_path):
    main_image1 = io.imread(image1_path)
    main_image2 = io.imread(image2_path)
    print(main_image1)
    main_image1_gray = rgb2gray(main_image1)
    main_image2_gray = rgb2gray(main_image2)

    (score,difference) = compare_ssim(main_image1_gray,main_image2_gray,full=True)
    print(score)
    print(difference)
    difference = (difference*255).astype("uint8")
    thresh = threshold_otsu(difference)

    cnts = find_contours(difference,thresh)
    different_image = main_image1
    for cnt in cnts:
        different_image = drawShape(different_image,cnt,[255,0,0])

    return different_image

myimg = find_difference_in_image('testing1.jpeg','testing2.jpeg')
io.imshow(myimg)
io.show()






# main_image1 = io.imread('testing1.png')
# main_image2 = io.imread('testing2.png')

# print(main_image1.shape)
# print(main_image2.shape)

# # io.imshow(main_image1)


# main_image1_gray = rgb2gray(main_image1)
# main_image2_gray = rgb2gray(main_image2)

# (score,difference) = compare_ssim(main_image1_gray,main_image2_gray,full=True)
# difference = (difference*255).astype("uint8")
# thresh = threshold_otsu(difference)

# cnts = find_contours(difference,thresh)

# # def drawShape(img,coordinates,color):
# #     img = gray2rgb(img)
# #     coordinates = coordinates.astype(int)

# #     img[coordinates[:, 0],coordinates[:, 1]] = color

# #     return img

# #diffImg = main_image1

# for cnt in cnts:
#     main_image2_gray = drawShape(main_image2,cnt,[255,0,0])

# io.imshow(main_image2_gray)
# io.show()
# io.imshow(main_image1_gray)
# io.show()








# io.show()

# print(main_image1_gray.shape)
# print(main_image2_gray.shape)

# io.imshow(main_image1_gray)
# io.show()

# #pix.writeImage(r'E:\pdfCompare\testimg.png',".png")

