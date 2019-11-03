import fourledsClass

import time
myled=forledsClass.FourLeds(27,11,23,15,14,22,24,23,17,10,9,25)
for i in range(138,2405,1):
    myled.changenumber(i)
    time.sleep(2)