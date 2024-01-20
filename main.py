import mainGUI as mg
from mainGUI import root
#MAIN
def showCamera():
    camera = mg.CameraGUI(master=root)
    camera.mainloop()

if __name__ == "__main__":
    showCamera()
    print("Application executed.")