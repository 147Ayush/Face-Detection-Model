import cv2 as c
from AppOpener import open, close

#Creating a video capture object, which help me to capture video through webcam
camera = c.VideoCapture(0, c.CAP_DSHOW)
#seting framewidth
camera.set(3,640)
#setting frameheight
camera.set(4,480)

#using Cascadeclassifier for effective detection of an object
detect = c.CascadeClassifier('frontalface.xml')


#taking unique id for every user
f_id = int(input("Enter numerical id: "))

#open camera
# b = "open camera"
# app_name = b.replace("open ", "")
# open(app_name, match_closest=True)

print("Take your face in front of webcam for sample")

count = 0
while True:
    ret, image = camera.read()#Reading Frames
    convert_img = c.cvtColor(image,c.COLOR_BGR2GRAY)#converting image to particular gray color for effective detection
    face = detect.detectMultiScale(convert_img,1.3, 5)
    for (x,y,z,h) in face:
        c.rectangle(image, (x,y), (x+z,y+h), (255,0,0), 2)#draw rectangle
        count += 1

        c.imwrite("sample/face." + str(f_id) + '.' + str(count) + ".jpg", convert_img[y:y+h,x:x+z])
        #capture image and save in sample folder with sequence name
        c.imshow('image',image)

    a = c.waitKey(100) & 0xff# wait for the pressed key
    if (a == 27): #press ESC to stop
        break
    elif (count >= 100):# take 20 samples
        break

print("Samples are taken now closing program")
# b = "close camera"
# app_name = b.replace("close ", "").strip()
# close(app_name, match_closest=True, output=False)
camera.release()
c.destroyAllWindows()



