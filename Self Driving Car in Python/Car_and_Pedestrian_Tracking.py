#import opencv(cv2)
import cv2

#image
img_file = 'hello.jpg'
video = cv2.VideoCapture('Tesla Dashcam Accident.mp4')

#getting the algo
car_tracker_file = 'cars.xml'

#create car classifier
car_tracker = cv2.CascadeClassifier(car_tracker_file)

while True:
    (read_successful, frame) = video.read()

    if read_successful:
        grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    else:
        break

    #detecting cars
    cars = car_tracker.detectMultiScale(grayscaled_frame)

    for (x,y,w,h) in cars:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)

    #displaying the image
    cv2.imshow('Self Driving Car in Python', frame)

    #method for the file to not close automatically
    key = cv2.waitKey(1)

    if key==81 or key==113:
        break

#release the videocapture object
video.release()

#code completed
print("Here is your self driving car")