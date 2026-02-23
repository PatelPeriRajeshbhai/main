import tkinter as tk
import cv2
from PIL import Image,ImageTk
from detector import facedetection

cap = None
detector = facedetection()

canvas = None
photo = None

def startcamera():
    global cap,canvas,photo
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        label.config(text="Camera is note open")
        return
    if canvas is None:
        canvas = tk.Canvas(root,width=640,height=480,bg="black")
        canvas.pack(pady=10)
    
    camera()   
def camera():
    global cap,photo
    
    if cap is None or not cap.isOpened():
        return
    
    ret,frame = cap.read()
    if not ret:
        label.config(text="Frame nahi aa rahi")
        return
    direction = detector.direction(frame)
    label.config(text="Direction: " + direction)
    frame = cv2.flip(frame,1)
   
    frame = cv2.resize(frame,(640, 480))              
    frame_rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)  
    img = Image.fromarray(frame_rgb)
    photo = ImageTk.PhotoImage(image=img)               
    
    canvas.delete("all")                                
    canvas.create_image(0,0,anchor=tk.NW,image=photo)
    direction = detector.direction(frame)
    label.config(text="Direction: " + direction)
    
    if cv2.waitKey(1) == 27:
        cap.release()
        cv2.destroyAllWindows()
        cap = None
        label.config(text="Direction:Camera off")
        return
root = tk.Tk()
root.title("Face Direction Detection")
canvas = tk.Canvas(root, width=640,height=480,bg="black")   
canvas.pack(pady=10)
label = tk.Label(root,text="Direction:")
label.pack()
start_btn = tk.Button(root,text="Start Camera",command=startcamera)
start_btn.pack()
root.mainloop()



