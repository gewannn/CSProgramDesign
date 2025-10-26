#程序功能：打开摄像头，捕获图像，识别图中物体，如果识别物体的可信度较高，则在图上标注物体名称
#运行方式：打开IDLE，File菜单的Open打开当前源文件，按F5运行
#按ESC退出程序

import os
import cv2
import numpy as np

path = os.path.dirname(__file__)
os.chdir(path)

rows = open("synsetwords.txt").read().strip().split("\n")
classes = [r[r.find(" ") +1:].split(",")[0] for r in rows]

net = cv2.dnn.readNetFromCaffe("ResNet50.prototxt", "ResNet50.caffemodel") #加载模型

cam = cv2.VideoCapture(0) #打开摄像头

while True:
    retval, image = cam.read()
    if not retval or image is None:
        break
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (224, 224)), 1, (224, 224), (104, 117, 123)) #预处理

    net.setInput(blob)
    preds = net.forward()
    idxs = np.argsort(preds[0])[::-1][:3]

    for (i, idx) in enumerate(idxs):
        score = float(preds[0][idx]) #可信度
        if i == 0 and preds[0][idx] >= 0.3: #排名第一，且可信度不小于30%
            text = "{}, {:.2%}".format(classes[idx], preds[0][idx])
            cv2.putText(image, text, (5, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2) #叠加文字
        
        if score >= 0.3: #可信度不小于30%进行输出
            print("[{}] {}, {:.2%}".format(i+1, classes[idx], preds[0][idx]))
    
    cv2.imshow("Image", image)

    if cv2.waitKey(1) == 27: #按ESC退出
        break
cv2.destroyAllWindows()