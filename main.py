import scipy.ndimage as sp
import cv2 
from skimage.metrics import structural_similarity as ssim
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import numpy as np

cameraId = 0

def capture(image):
    cv2.imshow("Captured image", image)
    _, _, width, _ = cv2.getWindowImageRect("Captured image") # Get the width of the image
    cv2.moveWindow("Captured image", width, 0)
    cv2.imwrite("capture.png", image)
    cv2.waitKey(0)
    return image

def compare(captureImg, image):    #image1 is the captured image and image2 is the image to be compared with
    ssim_rs = ssim(captureImg, image)
    mse_rs = mean_squared_error(captureImg, image)

    print("SSIM: {}, MSE: {}".format(ssim_rs, mse_rs))

def gauss(size, stddev, k):
    ker = np.zeros((size, size))
    mid = (size - 1)//2

    for i in range(size):
        for j in range(size):
            r = np.sqrt((i - mid)**2 + (j - mid)**2)
            ker[i][j] = k*np.exp((-r**2)/(2*(stddev**2)))
    ker = ker/np.sum(ker)
    return ker

def main():
    vid = cv2.VideoCapture(cameraId)
    capturedFlag = False
    captureImg = None
    gaussKer = gauss(11, 25, 1)
    while True:
        _, image = vid.read()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = sp.convolve(image, gaussKer)
        image = np.array(image, dtype = 'uint8')
        cv2.imshow("Video Handler", image)
        cv2.moveWindow("Video Handler", 0, 0)
        if (cv2.waitKey(1) & 0xFF) == ord(' '):
            captureImg = capture(image)
            capturedFlag = True
        elif (cv2.waitKey(1) & 0xFF) == ord('q'):
            break
        if capturedFlag:
            compare(captureImg, image)
    vid.release()        
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()