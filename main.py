import cv2
import mediapipe as mp
import time
import Finger

# Finger objects
Thumb = Finger()
Index = Finger()
Middle = Finger()
Ring = Finger()
Pinky = Finger()


def main():

    # captures video from webcam
    # NOTE: input value can vary between -1, 0, 1, 2 (differs per device, 0 or 1 is common)
    # WARNING: VideoCapture does not work if another application is using camera (ie. video calling)
    cap = cv2.VideoCapture(0)

    # from pre-trained Mediapipe to draw hand landmarks and connections
    mpHands = mp.solutions.hands
    hands = mpHands.Hands(max_num_hands=1)
    mpDraw = mp.solutions.drawing_utils

    # used to calculate FPS
    pTime = 0  # previous time
    cTime = 0  # current time

    while True:
        # reads image from webcam
        success, img = cap.read()

        # converts default image value to RGB value
        # NOTE: when printing back to the screen, use default value (img) NOT imgRGB
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        imgRGB.flags.writeable = False  # improves performance
        # use Mediapipe to process converted RGB value
        results = hands.process(imgRGB)

        if results.multi_hand_landmarks:

            for handLms in results.multi_hand_landmarks:
                # creates list of all landmarks for easier indexing
                # list will have 21 values -> lmList[0] will be first landmark
                lmList = []

                # id corresponds to landmark #
                #   -> 21 landmarks in total (4 on non-thumb fingers, rest on thumb and palm)
                # lm corresponds to landmark value
                #   -> each lm has x coordinate and y coordinate
                #   -> default values are in ratio (value between 0 and 1)
                #   -> to convert to pixel value, multiple by width and height of screen
                for id, lm in enumerate(handLms.landmark):
                    h, w, c = img.shape                 # get height, width, depth
                    # convert to x, y pixel values
                    cx, cy = int(lm.x*w), int(lm.y*h)

                    lmList.append([id, cx, cy])

                # draw hand landmarks and connections
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

        # print FPS on screen (not console)
        # cTime = time.time()
        # fps = 1/(cTime-pTime)
        # pTime = cTime
        # cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (0,0,255), 3)

        # print current image captured from webcam
        cv2.imshow("Image", img)
        key = cv2.waitKey(1)

        # press Q to quit or "stop" button
        if key == ord("q"):
            break

    # cleanup
    cap.release()
    cv2.destroyAllWindows()


main()
