import cv2
import os

cap = cv2.VideoCapture('D:\AIGC小组会\plant anything into any video\place-anything.github.io\static\Archive\sora_sea.mp4')
ret, frame = cap.read()
cv2.imwrite('sora_sea.png', frame)