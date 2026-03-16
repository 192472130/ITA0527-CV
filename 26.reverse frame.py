import cv2

video_path = r"C:\Users\jithe\OneDrive\Documents\opencv\3320517-hd_720_1280_25fps.mp4"

cap = cv2.VideoCapture(video_path)
frames = []

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)

cap.release()

for frame in reversed(frames):
    cv2.imshow("Reverse Video", frame)
    if cv2.waitKey(30) & 0xFF == 27:
        break

cv2.destroyAllWindows()
