#程序功能：打开摄像头，捕获图像，识别图中的人脸，在四周画框，并显示在窗口中
#运行方式：打开IDLE，File菜单的Open打开当前源文件，按F5运行
#异常情况：若未安装opencv库，将自动安装，shell中会显示下载进度
#按ESC退出程序

import os
try:
    import cv2
except:
    os.system("pip install opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple")
    import cv2

path = os.path.dirname(__file__)
os.chdir(path)

haarfile = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
facedetector = cv2.CascadeClassifier(haarfile) #加载脸部级联分类器

print("Open camera,please wait...",end="")
cam = cv2.VideoCapture(0) #打开摄像头

if not cam.isOpened():
    print("\nCamera not found")
else:
    print("\nCamera opened successfully")
    roi_face = None
    while True:
        retval, image = cam.read() #从摄像头捕获一幅图像
        if not retval or image is None: #捕获图像失败
            print("cam.read() 错误") #显示错误信息并退出
            break
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #转换为灰度
        faces = facedetector.detectMultiScale(gray, 1.1, 5) #检测脸部 
        for (x, y, w, h) in faces: #枚举所有脸
            roi_face = image[y:y+h, x:x+w].copy() #切分出脸部图像
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2) #在脸部四周画绿框
        cv2.imshow("Camera",image) #在窗口显示图像
        if cv2.waitKey(1) == 27: #按ESC键退出
            if roi_face is not None:
                cv2.imwrite("face.jpg", roi_face) #保存脸部图像
                break
    cv2.destroyAllWindows() #关闭窗口