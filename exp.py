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


class testclass:
    def __init__(self, a1,a2):
        self.a1 = a1
        self.a2 = a2
    def func(self):
        b = self.a1+1
        print(b)
a=testclass(1)
a.func()
# pdfPath = r'C:\ISIS\afpds\amacln5.pdf'
# imageName = r'amacln5image'
# def converPDFtoImage(pdfPath,imagePath,pageNo):
#     filename = os.path.basename(pdfPath)
#     if(os.path.isfile(pdfPath) and (filename[-4:]!='.pdf') or (filename[-4:]!='.PDF')):
#         doc = fitz.open(pdfPath)
#         page = doc.loadPage(pageNo)
#         pix = page.getPixmap(alpha=False)
#         img = Image.frombuffer("RGB", [pix.width, pix.height], pix.samples,"raw", "RGB", 0, 1)
#         RGB_numpy_image = np.array(img)
#         imageName = filename[:-4]
#         img.save(imageName+"%d.jpeg"%pageNo)
#         return img2
#     else:
#         print("Please enter a valid pdf path")

# a = converPDFtoImage(pdfPath,imageName,0)
# io.imshow(a)
# io.show()
# print(type(a))

