from Finger import Finger
from Landmark import Landmark

VERTICAL_ERROR_MARGIN = 10 # FOR FOUR FINGERS: number of pixels allowed to be considered same "level"

def createPositionTuple(lm_list):
    '''
    Input: landmark list of 21 landmarks
    Output: Tuple of (IndexPosition, MiddlePosition, RingPosition, PinkyPosition)
    
    Different Positions:
       -> 0: finger is all the way down
       -> 2: finger is all the way up
       -> 1: finger is between up and down (in the middle) 
    '''
    a = analyzeIndexFinger(lm_list)
    b = analyzeMiddleFinger(lm_list)
    c = analyzeRingFinger(lm_list)
    d = analyzePinkyFinger(lm_list)
    return (a, b, c, d)


def analyzeIndexFinger(lm_list):
    INDEX_FINGER_TIP = lm_list[8]
    INDEX_FINGER_DIP = lm_list[7]
    INDEX_FINGER_MCP = lm_list[5]

    if INDEX_FINGER_TIP[2] > INDEX_FINGER_MCP[2] or abs(
            INDEX_FINGER_TIP[2] - INDEX_FINGER_MCP[2]) < VERTICAL_ERROR_MARGIN:
        return 0
    elif INDEX_FINGER_TIP[2] < INDEX_FINGER_DIP[2]:
        return 2
    return 1


def analyzeMiddleFinger(lm_list):
    MIDDLE_FINGER_TIP = lm_list[12]
    MIDDLE_FINGER_DIP = lm_list[11]
    MIDDLE_FINGER_MCP = lm_list[9]

    if MIDDLE_FINGER_TIP[2] > MIDDLE_FINGER_MCP[2] or abs(
            MIDDLE_FINGER_TIP[2] - MIDDLE_FINGER_MCP[2]) < VERTICAL_ERROR_MARGIN:
        return 0
    elif MIDDLE_FINGER_TIP[2] < MIDDLE_FINGER_DIP[2]:
        return 2
    return 1


def analyzeRingFinger(lm_list):
    RING_FINGER_TIP = lm_list[16]
    RING_FINGER_DIP = lm_list[15]
    RING_FINGER_MCP = lm_list[13]

    if RING_FINGER_TIP[2] > RING_FINGER_MCP[2] or abs(
            RING_FINGER_TIP[2] - RING_FINGER_MCP[2]) < VERTICAL_ERROR_MARGIN:
        return 0
    elif RING_FINGER_TIP[2] < RING_FINGER_DIP[2]:
        return 2
    return 1


def analyzePinkyFinger(lm_list):
    PINKY_FINGER_TIP = lm_list[20]
    PINKY_FINGER_DIP = lm_list[19]
    PINKY_FINGER_MCP = lm_list[17]

    if PINKY_FINGER_TIP[2] > PINKY_FINGER_MCP[2] or abs(
            PINKY_FINGER_TIP[2] - PINKY_FINGER_MCP[2]) < VERTICAL_ERROR_MARGIN:
        return 0
    elif PINKY_FINGER_TIP[2] < PINKY_FINGER_DIP[2]:
        return 2
    return 1

def preprocess(lm_list, THUMB: Finger, INDEX: Finger, MIDDLE: Finger, RING: Finger, PINKY: Finger):
    for id, lm in enumerate(lm_list):

        # landmarks on the thumb
        if (id >= 1 and id <= 4):
            finger_num = id - 1
            THUMB.landmarks[finger_num] = Landmark(finger_num, lm[1], lm[2], lm[3])
            print("Finger: Thumb: ", "landmark: ", THUMB.landmarks[finger_num].id, "x:",
                    THUMB.landmarks[finger_num].x, "y:", THUMB.landmarks[finger_num].y, "z: ", THUMB.landmarks[finger_num].z,)

        # landmarks on index
        elif (id >= 5 and id <= 8):
            finger_num = id - 5
            INDEX.landmarks[finger_num] = Landmark(finger_num, lm[1], lm[2], lm[3])
            print("Finger: index: ", "landmark: ", INDEX.landmarks[finger_num].id, "x:",
                    INDEX.landmarks[finger_num].x, "y:", INDEX.landmarks[finger_num].y, "z: ", INDEX.landmarks[finger_num].z,)

        # landmarks on middle
        elif (id >= 9 and id <= 12):
            finger_num = id - 9
            MIDDLE.landmarks[finger_num] = Landmark(finger_num, lm[1], lm[2], lm[3])
            print("Finger: middle: ", "landmark: ", MIDDLE.landmarks[finger_num].id, "x:",
                    MIDDLE.landmarks[finger_num].x, "y:", MIDDLE.landmarks[finger_num].y, "z: ", MIDDLE.landmarks[finger_num].z,)

        # landmarks on fourth finger
        elif (id >= 13 and id <= 16):
            finger_num = id - 13
            RING.landmarks[finger_num] = Landmark(finger_num, lm[1], lm[2], lm[3])
            print("Finger: ring: ", "landmark: ", RING.landmarks[finger_num].id, "x:",
                    RING.landmarks[finger_num].x, "y:", RING.landmarks[finger_num].y, "z: ", RING.landmarks[finger_num].z,)

        # landmarks on fifth finger
        elif (id >= 17 and id <= 20):
            finger_num = id - 17
            PINKY.landmarks[finger_num] = Landmark(finger_num, lm[1], lm[2], lm[3])
            print("Finger: pinky: ", "landmark: ", PINKY.landmarks[finger_num].id, "x:",
                    PINKY.landmarks[finger_num].x, "y:", PINKY.landmarks[finger_num].y, "z: ", PINKY.landmarks[finger_num].z,)

def interpret(lm_list) -> 'string':

    THUMB = Finger()
    INDEX = Finger()
    MIDDLE = Finger()
    RING = Finger()
    PINKY = Finger()
    preprocess(lm_list, THUMB, INDEX, MIDDLE, RING, PINKY)
    
    fingerPositions = createPositionTuple(lm_list)

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
        return check_K_R_U_V(THUMB, INDEX, MIDDLE, RING, PINKY)
    elif fingerPositions == (2, 0, 0, 0):
        # If thumb out:
        # L
        # If landmark 8 is lower than 7
        # X
        # Else
        # D
        return check_L_X_D(lm_list)
    elif fingerPositions == (0, 2, 2, 2):
        #F
        return "F"
    elif fingerPositions == (0, 0, 0, 2):
        # If thumb out:
        #     Y
        # Else
        #     I
        return check_Y_I(THUMB, INDEX, MIDDLE, RING, PINKY)
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

def check_K_R_U_V(THUMB: Finger, INDEX: Finger, MIDDLE: Finger, RING: Finger, PINKY: Finger):
    #if (INDEX.landmarks[3].z - MIDDLE.landmarks[3].z) > 0.1:
    if abs(MIDDLE.landmarks[3].y - INDEX.landmarks[2].y) < 30:
        return "K"
    elif ((INDEX.landmarks[0].x > MIDDLE.landmarks[0].x and INDEX.landmarks[3].x < MIDDLE.landmarks[3].x) 
            or (INDEX.landmarks[0].x < MIDDLE.landmarks[0].x and INDEX.landmarks[3].x > MIDDLE.landmarks[3].x)):
        return "R"
    elif abs(INDEX.landmarks[3].x - MIDDLE.landmarks[3].x) < 60:
        return "U"
    else:
        return "V"

def check_L_X_D(lm_list):
    """
    :param lm_list: landmark of 21 landmarks
    :return: one of "L", "X", "Y" - all have same non-thumb finger positions (2, 0, 0, 0)
    """
    INDEX_TIP = lm_list[8]
    INDEX_DIP = lm_list[7]
    INDEX_PIP = lm_list[6]
    INDEX_MCP = lm_list[5]
    THUMB_TIP = lm_list[4]

    if INDEX_TIP[2] < INDEX_DIP[2]:
        if THUMB_TIP[1] > INDEX_MCP[1]:
            return "D"
        else:
            return "L"
    elif (abs(INDEX_TIP[2] - INDEX_DIP[2]) < VERTICAL_ERROR_MARGIN or abs(INDEX_TIP[2] - INDEX_PIP[2])) and THUMB_TIP[1] > INDEX_MCP[1]:
        return "X"
    return ""

def check_Y_I(THUMB: Finger, INDEX: Finger, MIDDLE: Finger, RING: Finger, PINKY: Finger):
    if(abs(THUMB.landmarks[3].x - THUMB.landmarks[0].x) > 40):
        return "Y"
    else:
        return "I"