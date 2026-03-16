import cv2
import pytesseract

cap = cv2.VideoCapture("video.mp4")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    text = pytesseract.image_to_string(frame)
    print(text)

    cv2.imshow("Frame",frame)
    if cv2.waitKey(1)==27:
        break
