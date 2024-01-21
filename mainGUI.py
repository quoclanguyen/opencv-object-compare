import tkinter as tk 
import videoHandler
import threading as tr

root = tk.Tk()
root.title("Image Processing")
root.geometry("1600x300")

#CAMERA gui
class CameraGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_video_capture()
    def create_video_capture(self):
        #create box for video capture 
        self.vid = videoHandler.capture()
        self.vid.pack(side="top")
        #create button to capture image
        self.capture = tk.Button(self, text="Capture", command=self.capture)
        self.capture.pack(side="bottom")