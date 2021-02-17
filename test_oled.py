import time
import sys
import os
from datetime import datetime
import random
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import Adafruit_SSD1306

def display_test(input_times):
    FONT_SIZE = 14
    
    disp = Adafruit_SSD1306.SSD1306_128_64(rst=0)
    
    disp.begin()
    disp.clear()
    disp.display()
    
    width = disp.width
    height = disp.height
    determine = []
    request_times = input_times
    answer=[]
    count=0
    image = Image.new('1', (width, height))
    draw = ImageDraw.Draw(image)
    font=ImageFont.truetype("./ARIALUNI.TTF",30)
    
    try:
        times = 1
        print('按下 Ctrl-C 可停止程式')
        while True:
            load = os.getloadavg()
            i=random.randint(0,100)
            draw.rectangle((0, 0, width, height), outline=0, fill=0)
            draw.text((0,0), str(i),font=font, fill=255)
            disp.image(image)
            disp.display()
            determine.append(i)
            time.sleep(1.5)
            if times == request_times:
                break
            else:
                times = times + 1
    except KeyboardInterrupt:
        print('關閉程式')
    finally:
        disp.clear()
        disp.display()
        for i in range(0,request_times):
            a=input("input:")
            answer.append(int(a))
        print("user answer: " + str(answer))
        print("correct answer: " + str(determine))
        for i in range(0,request_times):
            if(determine[i]==answer[i]):
                count=count+1
        print("match answer: " + str(count))
