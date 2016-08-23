import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('averagedimage.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
x = []
y = []

lines = cv2.HoughLines(edges,1,np.pi/180,200)
print "Here is the lines variable: ", lines
for rho,theta in lines[0]:
    x.append(rho)
    y.append(theta)
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)


ax = plt.subplot(111, projection='polar')
ax.plot(y, x, color='r', linewidth=2)
ax.grid(True)
plt.show()
cv2.imwrite('houghlines3.jpg',img)
