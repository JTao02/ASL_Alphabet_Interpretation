import cv2
import mediapipe as mp
import time
from Finger import Finger
from interpretation import interpret
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
ds_factor=0.6

class Camera():
    def __init__(self):
        print("BADDIEEEEE")
        self.video = cv2.VideoCapture(0)
        self.letters = "TEST"
        self.curr_time = time.time()
        self.prev_time = time.time()

    def __del__(self):
        self.video.release()
        cv2.destroyAllWindows()

    def add_space(self):
        self.letters += " "

    def delete(self):
        self.letters = self.letters[:-1]

    def clear(self):
        self.letters = ""

    def get_frame(self):

        # captures video from webcam
        # NOTE: input value can vary between -1, 0, 1, 2 (differs per device, 0 or 1 is common)
        # WARNING: VideoCapture does not work if another application is using camera (ie. video calling)
        cap = self.video

        # from pre-trained Mediapipe to draw hand landmarks and connections
        mpHands = mp.solutions.hands
        hands = mpHands.Hands(max_num_hands=1)
        mpDraw = mp.solutions.drawing_utils

        # used to calculate FPS
        # pTime = 0  # previous time
        # cTime = 0  # current time

        # used to record letter every 3 seconds hand is in frame
        self.prev_time = time.time()
        self.curr_time = time.time()

        # reads image from webcam
        _, img = cap.read()

        # converts default image value to RGB value
        # NOTE: when printing back to the screen, use default value (img) NOT imgRGB
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        imgRGB.flags.writeable = False  # improves performance
        # use Mediapipe to process converted RGB value
        results = hands.process(imgRGB)

        if results.multi_hand_landmarks:

            for handLms in results.multi_hand_landmarks:
                # creates list of all landmarks for easier indexing
                # list will have 21 values -> lm_list[0] will be first landmark
                lm_list = []

                # id corresponds to landmark #
                #   -> 21 landmarks in total (4 on non-thumb fingers, rest on thumb and palm)
                # lm corresponds to landmark value
                #   -> each lm has x coordinate and y coordinate
                #   -> default values are in ratio (value between 0 and 1)
                #   -> to convert to pixel value, multiple by width and height of screen
                for id, lm in enumerate(handLms.landmark):
                    h, w, c = img.shape                 # get height, width, depth
                    # convert to x, y pixel values
                    cx, cy, cz = int(lm.x*w), int(lm.y*h), lm.z*c

                    lm_list.append([id, cx, cy, cz])

                # writes text to screen
                cv2.putText(img, str(interpret(lm_list)), (550, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)

                # draw hand landmarks and connections
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

                # countdown timer
                self.curr_time = time.time()
                diff_time = self.curr_time - self.prev_time
                print(self.curr_time, self.prev_time)
                if diff_time < 1:
                    display_time = 3
                elif diff_time < 2:
                    display_time = 2
                elif diff_time <= 3:
                    display_time = 1
                cv2.putText(img, str(display_time), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (0,0,255), 3)
        else:
            # reset timer when hand not in frame
            print("BAD")
            self.prev_time = time.time()
        
        # capture letter of hand every three seconds
        self.curr_time = time.time()
        if self.curr_time - self.prev_time > 3:
            try:
                self.letters += interpret(lm_list)
            except TypeError:
                pass
            cv2.putText(img, "captured", (400,450), cv2.FONT_HERSHEY_PLAIN, 3, (66, 245, 102), 3)
            self.prev_time = time.time()
        
        cv2.putText(img, self.letters, (30,100), cv2.FONT_HERSHEY_PLAIN, 3, (66, 245, 102), 3)

        
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
            return None

        #############
        # img=cv2.resize(img,None,fx=ds_factor,fy=ds_factor,interpolation=cv2.INTER_AREA)
        # gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        # face_rects=face_cascade.detectMultiScale(gray,1.3,5)
        # for (x,y,w,h) in face_rects:
        # 	cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        # 	break
        ret, jpeg = cv2.imencode('.jpg', img)
        return jpeg.tobytes()