from Finger import Finger
from Landmark import Landmark

VERTICAL_ERROR_MARGIN = 10 # FOR FOUR FINGERS: number of pixels allowed to be considered same "level"

def createPositionTuple(lmList):
    '''
    Input: landmark list of 21 landmarks
    Output: Tuple of (IndexPosition, MiddlePosition, RingPosition, PinkyPosition)
    
    Different Positions:
       -> 0: finger is all the way down
       -> 2: finger is all the way up
       -> 1: finger is between up and down (in the middle) 
    '''
    a = analyzeIndexFinger(lmList)
    b = analyzeMiddleFinger(lmList)
    c = analyzeRingFinger(lmList)
    d = analyzePinkyFinger(lmList)
    return (a, b, c, d)


def analyzeIndexFinger(lmList):
    INDEX_FINGER_TIP = lmList[8]
    INDEX_FINGER_DIP = lmList[7]
    INDEX_FINGER_MCP = lmList[5]

    if INDEX_FINGER_TIP[2] > INDEX_FINGER_MCP[2] or abs(
            INDEX_FINGER_TIP[2] - INDEX_FINGER_MCP[2]) < VERTICAL_ERROR_MARGIN:
        return 0
    elif INDEX_FINGER_TIP[2] < INDEX_FINGER_DIP[2]:
        return 2
    return 1


def analyzeMiddleFinger(lmList):
    MIDDLE_FINGER_TIP = lmList[12]
    MIDDLE_FINGER_DIP = lmList[11]
    MIDDLE_FINGER_MCP = lmList[9]

    if MIDDLE_FINGER_TIP[2] > MIDDLE_FINGER_MCP[2] or abs(
            MIDDLE_FINGER_TIP[2] - MIDDLE_FINGER_MCP[2]) < VERTICAL_ERROR_MARGIN:
        return 0
    elif MIDDLE_FINGER_TIP[2] < MIDDLE_FINGER_DIP[2]:
        return 2
    return 1


def analyzeRingFinger(lmList):
    RING_FINGER_TIP = lmList[16]
    RING_FINGER_DIP = lmList[15]
    RING_FINGER_MCP = lmList[13]

    if RING_FINGER_TIP[2] > RING_FINGER_MCP[2] or abs(
            RING_FINGER_TIP[2] - RING_FINGER_MCP[2]) < VERTICAL_ERROR_MARGIN:
        return 0
    elif RING_FINGER_TIP[2] < RING_FINGER_DIP[2]:
        return 2
    return 1


def analyzePinkyFinger(lmList):
    PINKY_FINGER_TIP = lmList[20]
    PINKY_FINGER_DIP = lmList[19]
    PINKY_FINGER_MCP = lmList[17]

    if PINKY_FINGER_TIP[2] > PINKY_FINGER_MCP[2] or abs(
            PINKY_FINGER_TIP[2] - PINKY_FINGER_MCP[2]) < VERTICAL_ERROR_MARGIN:
        return 0
    elif PINKY_FINGER_TIP[2] < PINKY_FINGER_DIP[2]:
        return 2
    return 1

def preprocess(lmList, THUMB: Finger, INDEX: Finger, MIDDLE: Finger, RING: Finger, PINKY: Finger):
    for id, lm in enumerate(lmList):
        # # get height, width, depth or color(?)
        # h, w, c = img.shape
        # # convert to x and y pixel values
        # cx, cy = int(lm.x*w), int(lm.y*h)

        # landmarks on the thumb
        if (id > 0 and id < 5):
            finger_num = id - 1
            THUMB.landmarks[finger_num] = Landmark(id, lm.x, lm.y, lm.z)
            # print("Finger: Thumb: ", "Landmark: ", THUMB.landmark[id].id, "x:",
            #         THUMB.landmark[id].x, "y:", THUMB.landmark[id].y, "z: ", THUMB.landmark[id].z,)

        # landmarks on index
        elif (id > 4 and id < 9):
            finger_num = id - 5
            INDEX.landmarks[finger_num] = Landmark(finger_num, lm.x, lm.y, lm.z)
            # print("Finger: index: ", "landmark: ", INDEX.landmarks[finger_num].id, "x:",
            #         INDEX.landmarks[finger_num].x, "y:", INDEX.landmarks[finger_num].y, "z: ", INDEX.landmarks[finger_num].z,)

        # landmarks on middle
        elif (id > 8 and id < 13):
            finger_num = id - 9
            MIDDLE.landmarks[finger_num] = Landmark(finger_num, lm.x, lm.y, lm.z)
            # print("Finger: middle: ", "landmark: ", MIDDLE.landmarks[finger_num].id, "x:",
            #         MIDDLE.landmarks[finger_num].x, "y:", MIDDLE.landmarks[finger_num].y, "z: ", MIDDLE.landmarks[finger_num].z,)

        # landmarks on fourth finger
        elif (id > 12 and id < 17):
            finger_num = id - 24
            RING.landmarks[finger_num] = Landmark(finger_num, lm.x, lm.y, lm.z)
            # print("Finger: ring: ", "landmark: ", RING.landmarks[finger_num].id, "x:",
            #         RING.landmarks[finger_num].x, "y:", RING.landmarks[finger_num].y, "z: ", RING.landmarks[finger_num].z,)

        # landmarks on fifth finger
        else:
            finger_num = id - 17
            PINKY.landmarks[finger_num] = Landmark(finger_num, lm.x, lm.y, lm.z)
            # print("Finger: pinky: ", "landmark: ", PINKY.landmark[finger_num].id, "x:",
            #         PINKY.landmarks[finger_num].x, "y:", PINKY.landmarks[finger_num].y, "z: ", PINKY.landmarks[finger_num].z,)

def interpret(lmList) -> 'string':

    THUMB = Finger()
    INDEX = Finger()
    MIDDLE = Finger()
    RING = Finger()
    PINKY = Finger()
    preprocess(lmList, THUMB, INDEX, MIDDLE, RING, PINKY)
    
    fingerPositions = createPositionTuple(lmList)

    if fingerPositions == (2, 2, 2, 2):
        #B
        return "B"
    elif fingerPositions == (2, 2, 2, 0):
        #W
        return "W"
    elif fingerPositions == (2, 2, 0, 0):
        # If depth of middle finger is closer to camera:
        # K
        # If index tip is crossing middle tip:
        # R
        # If index tip is near middle tip:
        # U
        # Else:
        # V
        pass
    elif fingerPositions == (2, 0, 0, 0):
        # If thumb out:
        # L
        # If landmark 8 is lower than 7
        # X
        # Else
        # D
        pass
    elif fingerPositions == (0, 2, 2, 2):
        #F
        return "F"
    elif fingerPositions == (0, 0, 0, 2):
        # If thumb out:
        #     Y
        # Else
        #     I
        pass
    elif fingerPositions == (1, 1, 1, 1):
        #E
        return "E"
    elif fingerPositions == (1, 1, 1, 0):
        #M
        return "M"
    elif fingerPositions == (1, 1, 0, 0):
        #N
        return "N"
    elif fingerPositions == (0, 0, 0, 0):
        # If thumb right of index finger:
        # A
        # If thumb is horizontal:
        # S
        # Else: (Might need to change to t being behind index finger)
        # T
        pass

    else:
        #C and O
        #P and Q
        #G and H
        pass