import cv2
import numpy as np

def blur(image):
    img = cv2.imread(image)
    kernel = np.ones((5, 5), np.float32) / 25
    dst = cv2.filter2D(img, -1, kernel)
    cv2.imwrite('averagedimage.jpg', img)


def houghTransform(image):
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    x = []
    y = []

    lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
    print "Here is the lines variable: ", lines
    for rho, theta in lines[0]:
        x.append(rho)
        y.append(theta)
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho

        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))

        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

    cv2.imwrite('houghlines3.jpg', img)

blur('images/test.jpg')
houghTransform('averagedimage.jpg')

