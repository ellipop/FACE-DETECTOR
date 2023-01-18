# Importar la biblioteca OpenCV
import cv2

# Definir un objeto de captura de video
vid = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:/Users/user/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0/LocalCache/local-packages/Python310/site-packages/cv2/data/haarcascade_eye.xml')

while(True):
   
    # Capturar el video cuadro por cuadro
    ret, frame = vid.read()

    gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.1,5)
    eyes = eye_cascade.detectMultiScale(gray,1.1,5)


    for (x,y,w,h) in faces:
       cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    for (x,y,w,h) in eyes:
       cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)


    # Mostrar el cuadro resultante 
    cv2.imshow("Camara web", frame) # OpenCV no acepta caracteres especiales como el acento en "Cámara"
      
    # Salir de la ventana a través de la barra espaciadora
    if cv2.waitKey(25) == 32:
        break
  
# Después del bucle, liberar el objeto capturado
vid.release()

# Destruir todas las ventanas
cv2.destroyAllWindows()