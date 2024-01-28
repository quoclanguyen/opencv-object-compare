import cv2
import numpy as np
import matplotlib.pyplot as plt

x_pt_cache, y_pt_cache = 0, 0
x_pt, y_pt = -1, -1
def grabcut_algorithm(original_image, bounding_box):

    segment = np.zeros(original_image.shape[:2],np.uint8)  # Create a mask image of size (w,h)
    
    x,y,width,height = bounding_box # Create a rectangle of same size with full of zeros
    segment[y:y+height, x:x+width] = 1  # Make the region of interest in a mask image with 1

    background_mdl = np.zeros((1,65), np.float64)   # Create a array of size (1,65) with zeros
    foreground_mdl = np.zeros((1,65), np.float64)   # Create a array of size (1,65) with zeros
    
    cv2.grabCut(original_image, segment, bounding_box, background_mdl, foreground_mdl, 5,   
    cv2.GC_INIT_WITH_RECT)  # Apply grabcut algorithm with rectangle method

    new_mask = np.where((segment==2)|(segment==0),0,1).astype('uint8')  # Create a mask image with 0 and 1
    original_image = original_image*new_mask[:,:,np.newaxis]    # Apply the mask image on the original image
    cv2.imshow('Result', original_image)

def draw_bounding_box(click, x, y, flag_param, parameters):
    global x_pt, y_pt, drawing, top_left_point, bottom_right_point, original_image, cached_image, image
    global x_pt_cache, y_pt_cache
    if click == cv2.EVENT_LBUTTONDOWN: # Left button click
        drawing = True
        x_pt, y_pt = x, y 
    elif click == cv2.EVENT_MOUSEMOVE:
        if drawing:
            if x_pt_cache > x or y_pt_cache > y: #check the previous point is greater than the current point
                image = cached_image.copy()     #if yes, then delete the bounding box
            top_left_point, bottom_right_point = (x_pt,y_pt), (x,y)
            x_pt_cache, y_pt_cache = bottom_right_point         # Cache the bottom right point
            image = cached_image.copy()
            cv2.rectangle(image, top_left_point, bottom_right_point, (0,255,0), 2) # Draw rectangle on the image

    elif click == cv2.EVENT_LBUTTONUP:
        drawing = False
        top_left_point, bottom_right_point = (x_pt,y_pt), (x,y)
        cv2.rectangle(image, top_left_point, bottom_right_point, (0,255,0), 2)
        if top_left_point[0] > bottom_right_point[0]:   #check every way to draw the bounding box
                x_pt, x = x, x_pt
        if top_left_point[1] > bottom_right_point[1]:
                y_pt, y = y, y_pt
        bounding_box = (x_pt, y_pt, x-x_pt, y-y_pt) 
        grabcut_algorithm(original_image, bounding_box)
    #delete the bounding box
        image = cached_image.copy()
    
if __name__=='__main__':
    drawing = False
    top_left_point, bottom_right_point = (-1,-1), (-1,-1)

    original_image = cv2.imread("robert.png")
    
    original_image = cv2.resize(original_image ,(500,500)) # Resize image
    cached_image = original_image.copy()
    image = original_image.copy() # Make a copy of original image to draw bounding box
    cv2.namedWindow('Frame')
    cv2.setMouseCallback('Frame', draw_bounding_box)

    while True:
        cv2.imshow('Frame', image)
        c = cv2.waitKey(1)
        if c == 27:
            break
    cv2.destroyAllWindows()