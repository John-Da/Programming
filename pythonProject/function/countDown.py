import time


def countDown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = "{:02d}:{:02d}".format(mins, secs)
        time.sleep(1)
        print(timer, end="\r")
        t -= 1
    return False
