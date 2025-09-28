import os
from datetime import datetime
import cv2

path = os.path.dirname(os.path.abspath(__file__))
os.chdir(path)

print("Open camera, please waiting...", end="")
cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("Camera not found")
    exit(1)

print("Camera opened successfully")

cam.set(3, 1920)  # 宽度
cam.set(4, 1080)  # 高度

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("test.mp4", fourcc, 10, (1920, 1080))

while True:
    retval, image = cam.read()
    if not retval or image is None:
        print("cam.read() error")
        break

    timestr = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cv2.putText(image, timestr, (5, 25), cv2.FONT_HERSHEY_SIMPLEX, #右上角坐标大致1480，25
                0.6, (0, 0, 255), 1) #BGR蓝色255，0，0

    out.write(image)
    cv2.imshow("Camera", image)

    if cv2.waitKey(1) == 27:
        break

out.release()
cv2.destroyAllWindows()
