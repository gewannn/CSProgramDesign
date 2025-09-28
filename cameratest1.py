import os
import cv2 #下面几行注释要用的话先把这行删掉
#try:
    #import cv2
#except:
    #os.system("pip install openve-python -i ") 在外面写的，回家记得复制粘贴网址 懒得复制粘贴了就这样吧
    #import cv2
path = os.path.dirname(os.path.abspath(__file__))
os.chdir(path)

print("Open camera,please waiting...",end="")
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,1920)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,1080)#设置照片分辨率
print("the actual reaolution:",cam.get(cv2.CAP_PROP_FRAME_WIDTH),"x",cam.get(cv2.CAP_PROP_FRAME_HEIGHT))#检查摄像头实际分辨率

if not cam.isOpened():
    print("\nCamera not found")
    exit(1)
print("\nCamera opened successfully")
while True:
    retval, image = cam.read()
    if not retval or image is None:
        print("cam.read() error")
        break
    cv2.imshow("Camera",image)
    if cv2.waitKey(1) == 27:
        cv2.imwrite("test.jpg",image)
        break
cv2.destroyAllWindows()