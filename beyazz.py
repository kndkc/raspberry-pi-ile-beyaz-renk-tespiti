import cv2
import numpy as np
import RPi.GPIO as GPIO
import time #kütüphaneler çağırıldı

GPIO.setwarnings(False)   # hata mesajı kapatıldı

x=0   # cisim x koordinat değişkeni
y=0   # cisim y koordinat değişkeni
h=0   #cisim boyu
w=0   #cisim eni

cap = cv2.VideoCapture(0)  # alınan video cap değişkeine atandı

_, frame = cap.read()
rows, cols, _ = frame.shape

x_medium = int(cols / 2)
y_medium = int(cols / 2)
w_medium = int(cols / 2)
h_medium = int(cols / 2)
center = int(cols / 2)     # cizme ait x y h w bilgileri değişkenlere atandı

while True: # sonsuz döngüye girildi  
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # renk algilama işlemi başlatıldı
    
    low_BEYAZ = np.array([0, 0, 180])
    high_BEYAZ = np.array([0, 0, 255])
    red_mask = cv2.inRange(hsv_frame, low_BEYAZ, high_BEYAZ)  # renk bilgileri değişkenen atandı
    _, contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)    # renk algılanırsa işleme devam edilecek
    
    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt) # algılanan rengin x ve y koordinatları bulundu        
        x_medium = int((x + x + w) / 2)
        break
    cv2.rectangle(frame, (x, y), (x + w + 0, y + 0 + h), (0, 0, 255), 2)
    #beyaz cisimi dikdörtgen kutu içine alma              #kutu rengi #kutu kalınlığı
    
    cv2.imshow("iKiA MUHENDiSLiK ", frame)    
    print("x ",x+(w/2)," y ",y+(y/2))
    key = cv2.waitKey(1)
    
    if key == 20:   # renk olup olmadığı sorgulandı
        
        break
    
#cisim x ve y kordinatları shell ekranında float olarak akmaktadır