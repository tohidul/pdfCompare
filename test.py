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


pdfPath = r'C:\ISIS\afpds\amacln5.pdf'
imageName = r'amacln5image'

def converPDFtoImage(pdfPath,imagePath,pageNo):
    filename = os.path.basename(pdfPath)
    if(os.path.isfile(pdfPath) and (filename[-4:]!='.pdf') or (filename[-4:]!='.PDF')):
        doc = fitz.open(pdfPath)
        page = doc.loadPage(pageNo)
        pix = page.getPixmap(alpha=False)
        img = Image.frombuffer("RGB", [pix.width, pix.height], pix.samples,"raw", "RGB", 0, 1)
        imageName = filename[:-4]
        img.save(imageName+"%d.jpeg"%pageNo)
    else:
        print("Please enter a valid pdf path")
#converPDFtoImage(pdfPath,r'E:\pdfCompare',0)

def drawShape(img,coordinates,color):
    #img = gray2rgb(img)
    print(img.shape)
    coordinates = coordinates.astype(int)

    img[coordinates[:, 0],coordinates[:, 1]] = color

    return img


def find_difference_in_image(image1_path,image2_path):
    filename1 = os.path.basename(image1_path)
    #if(os.path.isfile(image1_path) and (filename1[-4:]!='.pdf') or (filename[-4:]!='.PDF')):
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

def compareImageByCoordinates(image1,image2,coordinates):
    if((type(image1) is np.ndarray) and (type(image2) is np.ndarray) and image1.shape==image2.shape):
        if(len(image1.shape)<2 or len(image1.shape)>2):
            print("compareImageByCoordinates function can only work with grayscale image and image shapes should be same")
        else:
            x1,y1,x2,y2,x3,y3,x4,y4 = coordinates
            while(y3<y1):
                while(x3<x1):
                    image1[y3][x3]=1
                    image2[y3][x3]=1
                    x3+=1
            y3+=1
            
    else:
        print("Image should in numpy array and equal in shape")

            


myimg = find_difference_in_image('amacln50_1.jpeg','amacln50_2.jpeg')
io.imshow(myimg)
io.show()
