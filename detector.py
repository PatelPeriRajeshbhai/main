import cv2
 
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
if face_cascade.empty():
    raise RuntimeError("Error: haarcascade_frontalface_default.xml file nahi mili")

class facedetection:
  def __init__(self):
    pass
  def direction(self,frame):
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    
    if len(faces) == 0:
      return "No Face"
    x,y,w,h = faces[0]
    cv2.rectangle(frame,(x,y),(x + w,y + h),(0,255,0),2)
    
    face_center_x = x + w // 2
    frame_center_x =frame.shape[1] // 2
    
    if face_center_x >frame_center_x  - 15:
      return "Looking Left"
    elif face_center_x <frame_center_x  +15:
        return "Looking Right"
    else:
      return "Looking Straight"
        
      

    
   
    
    

    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
       
        
      