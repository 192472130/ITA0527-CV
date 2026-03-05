import cv2
image = cv2.imread("virat kohli.jpg")
if image is None:
    print("Error: Image not found!")
    exit()
overlay = image.copy()
watermark_text = "© virat kohli"
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 2
thickness = 3
color = (255, 255, 255) 
(h, w) = image.shape[:2]
text_size = cv2.getTextSize(watermark_text, font, font_scale, thickness)[0]
text_x = w - text_size[0] - 20
text_y = h - 20
cv2.putText(overlay, watermark_text, (text_x, text_y),
            font, font_scale, color, thickness, cv2.LINE_AA)
alpha = 0.4
watermarked = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)
cv2.imshow("Original Image", image)
cv2.imshow("Watermarked Image", watermarked)
cv2.imwrite("watermarked_output.jpg", watermarked)
cv2.waitKey(0)
cv2.destroyAllWindows()