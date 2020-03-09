import time, cv2, requests
import numpy as np

url="http://26.39.224.75:8080/shot.jpg"

while True:
    img_resp=requests.get(url)
    img_arr=np.array(bytearray(img_resp.content),dtype=np.uint8)
    img=cv2.imdecode(img_arr,-1)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("AndroidCamera", gray_img)
    if cv2.waitKey(1)==27:
        break


