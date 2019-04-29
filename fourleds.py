#4 leds  pin(1-12)-BCM
#1-4  2-17 3-27 4-22  5-5   6-6
#7-19 8-21 9-20 10-16 11-12 12-18  
import time
import RPi.GPIO as GPIO
    #A  B  C  D  E F  G DP
A,B,C,D,E,F,G,DP,BIT0,BIT1,BIT2,BIT3=12,19,22,17,4,16,5,27,6,21,20,18
pins=[A,B,C,D,E,F,G,DP]
leds = [BIT0, BIT1, BIT2, BIT3]
n0=[A,B,C,D,E,F]
n1=[B,C]
n2=[A,B,G,E,D]
n3=[A,B,G,C,D]
n4=[F,G,B,C]
n5=[A,F,G,C,D]
n6=[A,F,E,D,C,G]
n7=[A,B,C]
n8=[A,B,C,D,E,F,G]
n9=[G,F,A,B,C,D]
ns=[n0,n1,n2,n3,n4,n5,n6,n7,n8,n9]

def setup():
	GPIO.setmode(GPIO.BCM)    #Number GPIOs by its physical location
	GPIO.setwarnings(False)
	for pin in pins:
		GPIO.setup(pin, GPIO.OUT)    #set all pins' mode is output
		GPIO.output(pin, GPIO.HIGH)  #set all pins are high level(3.3V)
	for b in leds:
                GPIO.setup(b,GPIO.OUT)
                GPIO.output(b,GPIO.HIGH)
            

def shownumber(x1,x2,x3,x4):#利用视觉暂留特性，依次显示各位数字，然后通过不断重复这个过程来显示4位数字
    c=[x1,x2,x3,x4]   
    for i in range(0,4,1):#show once
        GPIO.output(pins,0)
        GPIO.output(leds[0],i-0)
        GPIO.output(leds[1],i-1)
        GPIO.output(leds[2],i-2)
        GPIO.output(leds[3],i-3)
        GPIO.output(ns[c[i]],1)
        time.sleep(0.00001)#zan liu 0.0002second
    
if __name__=='__main__':
    setup()
    for number in range(1000,9999,1):
        z1=number%10#ge wei
        z2=int(number/10)%10#shi wei
        z3=int(number/100)%10# bai wei
        z4=int(number/1000)%10# qian wei
        for i in range(300):
            shownumber(z1,z2,z3,z4)
