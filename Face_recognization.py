import cv2 as c

recognize = c.face.LBPHFaceRecognizer.create()
recognize.read('Trained_model/model.yml')
faceCascade = c.CascadeClassifier('frontalface.xml')

font = c.FONT_HERSHEY_SIMPLEX

id = 2 #number of person you want to recognize

names = ['','Obhik']

cam = c.VideoCapture(0,c.CAP_DSHOW)# for removing warning
cam.set(3,640)#set video frameweight
cam.set(4,480)#set video frameheight

#define size of window to recognize face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

while True:
    ret, img = cam.read()
    convert_img = c.cvtColor(img,c.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(convert_img,scaleFactor=1.2,minNeighbors=5,minSize=(int(minW),int(minH)))

    for (x,y,z,h) in faces:
        c.rectangle(img,(x,y),(x+z,y+h), (0,255,0),2)#draw retangle
        id, accuracy = recognize.predict(convert_img[y:y+h,x:x+z])#predict every sample image
        accuracy = " {0}".format(round(100 - accuracy))
        #check accuracy
        if(int(accuracy) > 25):
            id = names[id]
            accuracy = accuracy + "%"
        else:
            id = "Unknown"
            accuracy = accuracy + "%"


        c.putText(img,str(id),(x+100,y-5), font, 1,(255,255,255),2)
        c.putText(img,str(accuracy),(x+5,y-5), font, 1,(255,255,255),2)

    c.imshow('camera',img)

    a = c.waitKey(10) & 0xff
    if a == 27:
        break

cam.release()
c.destroyAllWindows()