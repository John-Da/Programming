import time

delayTime = 5
def countdown(): 
    t = 1
    while t: 
        time.sleep(delayTime)
        t -= 1

countdown()