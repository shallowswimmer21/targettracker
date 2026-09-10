import cv2


def to_gry(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


def to_hsv(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


camera = cv2.VideoCapture(0)

# check if camera opened properly
if not camera.isOpened():
    print("Camera could not be opened")
    exit()


# take first frame to get width and height
success, frame = camera.read()

if not success:
    print("Could not read frame")
    exit()


# frame.shape gives height, width and number of colour channels
height, width, channels = frame.shape

# find centre of frame
centre_x = width // 2
centre_y = height // 2


while True:

    # read a new frame from camera
    success, frame = camera.read()

    if not success:
        break


    # convert clean frame before drawing anything on it
    gray = to_gry(frame)
    hsv = to_hsv(frame)


    # print the bgr values of pixel at x=120 and y=100
    print(frame[100, 120])

    # print the same pixel in grayscale
    print(gray[100, 120])

    # print the same pixel in hsv
    print(hsv[100, 120])


    # make a copy so drawing does not manipulate original frame
    display_frame = frame.copy()

    # draw circle at centre of frame
    cv2.circle(display_frame, (centre_x, centre_y), 5, (0, 0, 254), -1)


    # display original, grayscale and hsv images
    cv2.imshow("live feed", display_frame)
    cv2.imshow("gray", gray)
    cv2.imshow("hsv", hsv)


    # press q to stop program
    if cv2.waitKey(1) == ord("q"):
        break


# release camera and close windows
camera.release()
cv2.destroyAllWindows()