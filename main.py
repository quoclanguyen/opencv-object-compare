import cv2 

def capture(image):
    cv2.imshow("Captured image", image)
    _, _, width, _ = cv2.getWindowImageRect("Captured image")
    cv2.moveWindow("Captured image", width, 0)
    image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    cv2.imwrite("capture.png", image_gray) 
    cv2.waitKey(0)

def compare():
    return

def main():
    vid = cv2.VideoCapture(0)

    while True:
        _, image = vid.read()
        cv2.imshow("Video Handler", image)
        cv2.moveWindow("Video Handler", 0, 0)
        if (cv2.waitKey(1) & 0xFF) == ord(' '):
            capture(image)
        elif (cv2.waitKey(1) & 0xFF) == ord('q'):
            break
    vid.release()        
    cv2.destroyAllWindows()
if __name__=='__main__':
    main()