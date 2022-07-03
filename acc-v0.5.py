#v0.5
from __future__ import division
from plyer import notification
from PIL import ImageGrab,Image

import easyocr
import keyboard
import time
import re


def start():
    img1=ImageGrab.grabclipboard()
    if isinstance(img1, Image.Image):
        img1.save("result.png")
        reader = easyocr.Reader(['en'])   
        result = reader.readtext('result.png',min_size=0,text_threshold=0.3,low_text = 0.1)  
        l=[]
        for i in result:
            word = i[1]  
            word = ''.join(re.findall('[0-9]',word))
            l.append(word)
        try:    
            l.remove("")
        except ValueError:
            pass
        
        print(l)


        best=int(l[0])+int(l[1])
        cool=int(l[2])+int(l[3])
        good=int(l[4])
        miss=int(l[5])

        nbest=1
        ncool=3/4
        ngood=2/5
        nmiss=0

        result1=best*nbest+cool*ncool+good*ngood+miss*nmiss
        result2=nbest*(best+cool+good+miss)
        result_a=result1/result2

        print(result_a)

        notification.notify(
            title="ACC",
            message="您的acc在malody中是"+str(result_a),
            app_icon="tubiao.ico",
            timeout=5
        )
        
    else:
        print("请复制图片")

        
while True:
    if keyboard.is_pressed('F1'):
        time.sleep(1)
        start()
