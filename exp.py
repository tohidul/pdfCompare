from skimage import io
import numpy

a = numpy.array([[1,2,3],[1,2]])
b = numpy.array([1,2,3])
print(a.shape==b.shape)