import tkinter as tk 
import videoHandler
#CAMERA gui
class CameraGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_video_capture()
    def create_video_capture(self):
        #create box for video capture 
        self.vid = video.capture()
        self.vid.pack(side="top")
        #create button to capture image
        self.capture = tk.Button(self, text="Capture", command=self.capture)
        self.capture.pack(side="bottom")


#HISTOGRAM gui
class HistogramGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Histogram"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")
        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")
    def say_hi(self):
        print("hi there, everyone!")
#MAIN
root = tk.Tk()
root.title("Image Processing")
root.geometry("1600x300")
app = CameraGUI(master=root)
app = HistogramGUI(master=root)
app.mainloop()