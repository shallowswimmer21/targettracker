
import cv2

# Open the default camera
camera = cv2.VideoCapture(0)

print("Camera opened:", camera.isOpened())

# Get camera frame size
frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

print("Frame size:", frame_width, "x", frame_height)

# Define video codec
fourcc = cv2.VideoWriter_fourcc(*"mp4v")

# Create video writer
out = cv2.VideoWriter(
    "output.mp4",
    fourcc,
    30.0,
    (frame_width, frame_height)
)

while True:
    success, frame = camera.read()

    # Always check that the frame was captured successfully first
    if not success:
        print("Could not read frame")
        break

    # Save the frame to the output video
    out.write(frame)

    # Show the live camera feed
    cv2.imshow("Camera", frame)

    # Press q to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Cleanup happens AFTER the loop
camera.release()
out.release()
cv2.destroyAllWindows()
