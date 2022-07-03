#v0.2
from __future__ import division
import pyautogui
from plyer import notification

import easyocr  
import keyboard


while True:
    
    keyboard.wait('F1')

    result_l = pyautogui.locateOnScreen('get.png',grayscale=False,confidence=0.8)

    a1,a2,a3,a4=result_list=list(result_l)

    output=pyautogui.screenshot(imageFilename='result.png',region=[a1,a2,a3,a4])

    reader = easyocr.Reader(['en'])   
    result = reader.readtext('result.png')  
    l=[]
    for i in result:
        word = i[1]  
        l.append(word)


    best=int(l[2])+int(l[5])
    cool=int(l[8])+int(l[11])
    good=int(l[14])
    miss=int(l[17])


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