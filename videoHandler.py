# import the opencv library 
import cv2 

def capture():
    # define a video capture object 
    vid = cv2.VideoCapture(0) 

    while(True):
        _, image = vid.read()
            # showing result, it take frame name and image   
        cv2.imshow("sample_image", image)
        if cv2.waitKey(1):
            # saving image in local storage 
            image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
            #save image to path
            cv2.imwrite("sample_image.png", image_gray) 
            cv2.destroyWindow("sample_image") 
            break
    vid.release() # release the videocapture object
    # Destroy all the windows
    cv2.destroyAllWindows() # destrooy all the opened windows

def compare():
    # read gray scale image
    vid = cv2.VideoCapture(0) 
    image_gray = cv2.imread("sample_image.png", 0)
    while(True): 

    # Capture the video frame 
    # by frame 
        _, frame = vid.read() 
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        cv2.imshow('frame', frame)
        #compare image
        compare = image_gray == frame_gray
        if (cv2.waitKey(1) & 0xFF) == ord('q'): 
            break
        else:
            if compare.all():
                print("1")
            else:
                print("0")
            # Display the resulting frame 
            
            # the 'q' button is set as the 
            # quitting button you may use any 
            # desired button of your choice 
        
        # After the loop release the cap object 
    vid.release() # release the videocapture object
    # Destroy all the windows
    cv2.destroyAllWindows() # destroy all the opened windows