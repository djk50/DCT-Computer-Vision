import apriltag
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
detector = apriltag.Detector()

img = cv2.imread("data/Track 10-22/60_0.png", cv2.IMREAD_GRAYSCALE)

#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
result,img2 = detector.detect(img, return_image = True)
print(result)
cv2.imwrite("output.jpg",img2)

# while True:
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#
#     # Our operations on the frame come here
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     # Display the resulting frame
#     result = detector.detect(gray)
#     print(result)
#
#     # draw a bounding quadrilateral (optional)
#     if len(result) > 0:
#         pts = np.array(result[0].corners, dtype=np.int32)
#         pts = pts.reshape((-1, 1, 2))
#         cv2.polylines(gray, [pts], True, (255, 0, 0), 3)
#
#     # display image
#     cv2.imshow('frame', gray)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

