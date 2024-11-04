import sys
import time
def Countdown(n):
    for i in range(1,n+1):
        print(n-i+1)
        time.sleep(1)
    print("              BOOM!!!")
n = int(sys.argv[1])
Countdown(n)
