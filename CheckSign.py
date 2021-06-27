# from Finger import Finger
# from Landmark import Landmark
# from main import cv2, main
# import mediapipe as mp
# import time


# class CheckSign:
'''
    Checks sign
    '''

# Detects


# Check sign method
'''
def checkSigns(img):
    # Loop through 4
    isC = True
    isU = True
    isV = True
    isY = True
    isO = True

    for num in range(1, 5):

        # Lower index is the higher Landmark i think
        if((abs(thumb.landmarks[num].x-pinky.landmarks[num].x) > 0.08) or (abs(thumb.landmarks[num].y-pinky.landmarks[num].y) > 0.35)
                or (abs(thumb.landmarks[num].y-pinky.landmarks[num].y) < 0.15)):
            isC = False

            # Checking for U
        if((abs(index.landmarks[num].x-middle.landmarks[num].x) > 0.07) or (abs(index.landmarks[num].y-middle.landmarks[num].y) > 0.04)
            or (abs(index.landmarks[num].y-middle.landmarks[num].y) < 0.003) or
           (abs(index.landmarks[4].y-ring.landmarks[4].y) < 0.1) or (abs(index.landmarks[4].x-middle.landmarks[4].x)) > 0.05):
            isU = False

            # Checking for V
        if((abs(index.landmarks[num].y-middle.landmarks[num].y) > 0.06) or
           (abs(index.landmarks[4].y-ring.landmarks[4].y) < 0.1) or (abs(index.landmarks[4].x-middle.landmarks[4].x)) < 0.05):
            isV = False

            # Checking for Y
        if((thumb.landmarks[1].y < index.landmarks[4].y) or (thumb.landmarks[1].y < middle.landmarks[4].y)
           or (thumb.landmarks[1].y < ring.landmarks[4].y) or pinky.landmarks[1].y > thumb.landmarks[1].y or
           abs(pinky.landmarks[1].y-pinky.landmarks[4].y < 0.15) or abs(thumb.landmarks[1].y-thumb.landmarks[4].y < 0.15)):
            isY = False

            # Checking for o
        if((abs(thumb.landmarks[num].x-pinky.landmarks[num].x) > 0.07) or (abs(thumb.landmarks[num].y-pinky.landmarks[num].y) > 0.3)
                or (abs(thumb.landmarks[1].y-index.landmarks[1].y) > 0.18)):
            isO = False

    if (isC):
        # print("Letter C")
        cv2.putText(img, "C", (550, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0),
                    3)
    elif (isU):
        # print("Letter U")
        cv2.putText(img, "U", (550, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0),
                    3)
    elif (isV):
        # print("Letter V")
        cv2.putText(img, "V", (550, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0),
                    3)
    elif (isY):
        # print("Letter Y")
        cv2.putText(img, "Y", (550, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0),
                    3)
    elif (isO):
        # print("Letter O")
        cv2.putText(img, "O", (550, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0),
                    3)

'''


# In main

''' 
  counter += 1
                # Landmarks on the thumb
                    if (id > 0 and id < 5):
                        thumb.landmarks[id] = Landmark(id, lm.x, lm.y, lm.z)
                        print("Finger: Thumb: ", "Landmark: ", thumb.landmarks[id].id, "x:",
                              thumb.landmarks[id].x, "y:", thumb.landmarks[id].y, "z: ", thumb.landmarks[id].z,)

                    # Landmarks on index
                    if (id > 4 and id < 9):
                        fingerNum = id-4
                        index.landmarks[fingerNum] = Landmark(
                            fingerNum, lm.x, lm.y, lm.z)
                        print("Finger: index: ", "Landmark: ", index.landmarks[fingerNum].id, "x:",
                              index.landmarks[fingerNum].x, "y:", index.landmarks[fingerNum].y, "z: ", index.landmarks[fingerNum].z,)

                    # Landmarks on middle
                    if (id > 8 and id < 13):
                        fingerNum = id-8
                        middle.landmarks[fingerNum] = Landmark(
                            fingerNum, lm.x, lm.y, lm.z)
                        print("Finger: middle: ", "Landmark: ", middle.landmarks[fingerNum].id, "x:",
                              middle.landmarks[fingerNum].x, "y:", middle.landmarks[fingerNum].y, "z: ", middle.landmarks[fingerNum].z,)

                    # Landmarks on fourth finger
                    if (id > 12 and id < 17):
                        fingerNum = id-12
                        ring.landmarks[fingerNum] = Landmark(
                            fingerNum, lm.x, lm.y, lm.z)
                        print("Finger: ring: ", "Landmark: ", ring.landmarks[fingerNum].id, "x:",
                              ring.landmarks[fingerNum].x, "y:", ring.landmarks[fingerNum].y, "z: ", ring.landmarks[fingerNum].z,)

                    # Landmarks on fifth finger
                    if (id > 16 and id < 21):
                        fingerNum = id-16
                        pinky.landmarks[fingerNum] = Landmark(
                            fingerNum, lm.x, lm.y, lm.z)
                        print("Finger: pinky: ", "Landmark: ", pinky.landmarks[fingerNum].id, "x:",
                              pinky.landmarks[fingerNum].x, "y:", pinky.landmarks[fingerNum].y, "z: ", pinky.landmarks[fingerNum].z,)

                    if (counter > 30):
                        checkSigns(img)
'''
