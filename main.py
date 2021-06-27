from flask import Flask, render_template, Response
from Camera import Camera

app = Flask(__name__)


def add_space(text):
    return text + " "


def delete(text):
    return text[:-1]


def clear(text):
    return ""


def gen(camera):
    while True:
        frame = camera.get_frame()
        if not frame:
            camera.end()
            return
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


# if __name__ == "__main__":
#     app.run(host='0.0.0.0', debug=True)

# def main():

#     # captures video from webcam
#     # NOTE: input value can vary between -1, 0, 1, 2 (differs per device, 0 or 1 is common)
#     # WARNING: VideoCapture does not work if another application is using camera (ie. video calling)
#     cap = cv2.VideoCapture(0)

#     # from pre-trained Mediapipe to draw hand landmarks and connections
#     mpHands = mp.solutions.hands
#     hands = mpHands.Hands(max_num_hands=1)
#     mpDraw = mp.solutions.drawing_utils

#     # used to calculate FPS
#     # pTime = 0  # previous time
#     # cTime = 0  # current time

#     # used to record letter every 3 seconds hand is in frame
#     prev_time = time.time()
#     curr_time = time.time()

#     letters = ""

#     while True:
#         # reads image from webcam
#         _, img = cap.read()

#         # converts default image value to RGB value
#         # NOTE: when printing back to the screen, use default value (img) NOT imgRGB
#         imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         imgRGB.flags.writeable = False  # improves performance
#         # use Mediapipe to process converted RGB value
#         results = hands.process(imgRGB)

#         if results.multi_hand_landmarks:

#             for handLms in results.multi_hand_landmarks:
#                 # creates list of all landmarks for easier indexing
#                 # list will have 21 values -> lm_list[0] will be first landmark
#                 lm_list = []

#                 # id corresponds to landmark #
#                 #   -> 21 landmarks in total (4 on non-thumb fingers, rest on thumb and palm)
#                 # lm corresponds to landmark value
#                 #   -> each lm has x coordinate and y coordinate
#                 #   -> default values are in ratio (value between 0 and 1)
#                 #   -> to convert to pixel value, multiple by width and height of screen
#                 for id, lm in enumerate(handLms.landmark):
#                     h, w, c = img.shape                 # get height, width, depth
#                     # convert to x, y pixel values
#                     cx, cy, cz = int(lm.x*w), int(lm.y*h), lm.z*c

#                     lm_list.append([id, cx, cy, cz])

#                 # writes text to screen
#                 cv2.putText(img, str(interpret(lm_list)), (550, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)

#                 # draw hand landmarks and connections
#                 mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

#                 # countdown timer
#                 curr_time = time.time()
#                 diff_time = curr_time - prev_time
#                 if diff_time < 1:
#                     display_time = 3
#                 elif diff_time < 2:
#                     display_time = 2
#                 elif diff_time <= 3:
#                     display_time = 1
#                 cv2.putText(img, str(display_time), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (0,0,255), 3)
#         else:
#             # reset timer when hand not in frame
#             prev_time = time.time()

#         # capture letter of hand every three seconds
#         curr_time = time.time()
#         if curr_time - prev_time > 3:
#             try:
#                 letters += interpret(lm_list)
#             except TypeError:
#                 pass
#             cv2.putText(img, "captured", (400,450), cv2.FONT_HERSHEY_PLAIN, 3, (66, 245, 102), 3)
#             prev_time = time.time()

#         cv2.putText(img, letters, (30,100), cv2.FONT_HERSHEY_PLAIN, 3, (66, 245, 102), 3)


#         # print FPS on screen (not console)
#         # cTime = time.time()
#         # fps = 1/(cTime-pTime)
#         # pTime = cTime
#         # cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (0,0,255), 3)

#         # print current image captured from webcam
#         cv2.imshow("Image", img)
#         key = cv2.waitKey(1)

#         # press Q to quit or "stop" button
#         if key == ord("q"):
#             break

#     # cleanup
#     cap.release()
#     cv2.destroyAllWindows()


# main()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
