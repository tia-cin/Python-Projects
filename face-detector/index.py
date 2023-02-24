import cv2

picture = input("Please paste image with face: ")

cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
photo = cv2.imread("picture.png")

gray = cv2.cvtColor(photo, cv2.COLOR_RGB2GRAY)
faces = cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(photo, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow("photo", photo)
cv2.waitKey()

cv2.imwrite("face_detected.png", photo)