import cv2 as cv
import numpy as np

filePath = 'Chaeyoung20.jpg'
imgFlag = int(1)
image = cv.imread(filePath,imgFlag)

if(len(image.shape)<2):
    print('\nImage Type: Grayscale image')
    exit()
elif len(image.shape)==3:
    print('\nImage type: Colored Image')

Maxheight = 720
Maxwidth = 720
Minheight = 360
Minwidth = 360
Size = 1600000
print("\nImage Dimension limit: Maximum = 720 x 720 and Minimum = 360 x 360")
imageheight = image.shape[0]
imagewidth = image.shape[1]
print("Current loaded image dimension: ",imageheight,"x",imagewidth)
if((imageheight <= Maxheight and imageheight >= Minheight) and (imagewidth <= Maxwidth and imagewidth >= Minwidth)):
    print("Current loaded image is within the bounderies")
else:
    print("Current loaded image is not in the bounderies")

print("\nSet Size: ",Size)
imagesize = image.size
print("Current loaded image size: ",imagesize)
if(imagesize < Size):
    print("Currrent loaded image has Lower pixel count than the set image size")
else:
    print("Current loaded image has Higher pixel count than the set image size")

print("\nCurrent Loaded Image Datatype: ",image.dtype)

print("\nAccess a pixel value using item method")
a,b,c = input("Enter Row, Column and Channel: ").split()
row,column,channel = [int(a),int(b),int(c)]
result = image.item(row,column,channel)
print("Result: ",result)

print("\nModify a pixel value using itemset method")
d,e = input("Enter Row and Column: ").split()
blue = int(input("Enter changes in blue channel: "))
green = int(input("Enter changes in green channel: "))
red = int(input("Enter changes in red channel: "))
print("\nResult")
row1,column1 = [int(d),int(e)]
image.item(row1,column1,0)
image.item(row1,column1,1)
image.item(row1,column1,2)
result1 = image[row1,column1]
print("Before: ",result1)
image.itemset((row1,column1,0),blue)
image.itemset((row1,column1,1),green)
image.itemset((row1,column1,2),red)
result2 = image[row1,column1]
print("After: ",result2,"\n")

cv.imshow("CHAEYOUNG",image)
cv.waitKey(0)
cv.destroyAllWindows()