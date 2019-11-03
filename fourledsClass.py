import time
import RPi.GPIO as GPIO
import _thread
    #A  B  C  D  E F  G DP
class FourLeds:
    def __init__(self,A,B,C,D,E,F,G,DP,BIT0,BIT1,BIT2,BIT3):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        self.number=1111
        self.a=A
        self.b=B
        self.c=C
        self.d=D
        self.e=E
        self.f=F
        self.g=G
        self.dp=DP
        self.b0=BIT0
        self.b1=BIT1
        self.b2=BIT2
        self.b3=BIT3
        self.pins=[A,B,C,D,E,F,G,DP]
        self.leds = [BIT0, BIT1, BIT2, BIT3]
        self.n0=[A,B,C,D,E,F]
        self.n1=[B,C]
        self.n2=[A,B,G,E,D]
        self.n3=[A,B,G,C,D]
        self.n4=[F,G,B,C]
        self.n5=[A,F,G,C,D]
        self.n6=[A,F,E,D,C,G]
        self.n7=[A,B,C]
        self.n8=[A,B,C,D,E,F,G]
        self.n9=[G,F,A,B,C,D]
        self.ns=[self.n0,self.n1,self.n2,self.n3,self.n4,self.n5,self.n6,self.n7,self.n8,self.n9]
        for pin in self.pins:
            GPIO.setup(pin,GPIO.OUT)
            GPIO.output(pin,GPIO.HIGH)
        for p in self.leds:
            GPIO.setup(p,GPIO.OUT)
            GPIO.output(p,GPIO.HIGH)
        thread1=_thread.start_new_thread(self.shownumber,())
    def changenumber(self,number):
        self.number=number
    def shownumber(self):#利用视觉暂留特性，依次显示各位数字，然后通过不断重复这个过程来显示4位数字
        while True:
            z1=self.number%10#ge wei
            z2=int(self.number/10)%10#shi wei
            z3=int(self.number/100)%10# bai wei
            z4=int(self.number/1000)%10# qian wei
            c=[z4,z3,z2,z1]
            for i in range(0,4,1):#show once
                GPIO.output(self.pins,0)
                GPIO.output(self.leds[0],i-0)
                GPIO.output(self.leds[1],i-1)
                GPIO.output(self.leds[2],i-2)
                GPIO.output(self.leds[3],i-3)
                GPIO.output(self.ns[c[i]],1)
                time.sleep(0.00001)#zan liu 0.0002second
    
