import numpy as np
import cv2
import PoseModule as pm
import time
detector =pm.poseDector()
cap = cv2.VideoCapture('curls.mp4')
count = 0
dir = 0
pTime = 0
## Right Arm Biceps Curls
def RightArm(img ,draw = True):
    angle = detector.findAngle(img, 11 ,13 ,15)
    return angle
## Left Arm Biceps Curls
def LeftArm(img, draw = True):
    angle = detector.findAngle(img, 12, 14, 16)
    return angle

# def Squats():
#     pass
# hand_name =input("Enter The Hand : ")

while True:
    success, img = cap.read()
    img = cv2.resize(img, (1280,720))
    # img = cv2.imread("workoutImage.jpg")
    img = detector.findPose(img,False)
    lmList = detector.findPosition(img, False)
    # print(lmList) printing the landmark for testing
    if (len(lmList ) )!=0:
        #Right Arm

        angle = detector.findAngle(img, 11, 13 ,15)
        # print(angle)
        angle = RightArm(img)
        # print(angle)
        # angle = LeftArm(img)
        ## left Arm
        per = np.interp(angle, (210, 310), (0, 100))# here convert the angle
        bar = np.interp(angle, (220, 310),(650, 100))

        #check For Dumbbell curls
        color = (255, 0, 255)
        if per == 100:
            color = (0, 255 ,0)
            if dir == 0:
                count += 0.5

                dir = 1
        if per == 0:
            color = (0,255, 0)
            if dir == 1:
                count+= 0.5
                # print(count)
                dir =0

             # Draw Bar
        cv2.rectangle(img, (1100, 80), (1175, 650),color,3)
        cv2.rectangle(img, (1100, int(bar)),(1175 ,650),color, cv2.FILLED)
        cv2.putText(img, f'{int(per)}%' ,(170,150),cv2.FONT_HERSHEY_PLAIN, 10, (255 ,0 ,0) ,15)
            # Draw Curl Count
        cv2.rectangle(img, (0, 450), (250, 720), (0, 255, 0),cv2.FILLED)
        cv2.putText(img,str(int(count)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 10)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.imshow("Images", img)
    cv2.waitKey(1)
