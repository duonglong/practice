import sys
import time

for i in range(10):
    sys.stdout.write("\r" + "Loading" + "." * i)
    time.sleep(1)
    sys.stdout.flush()
#print()
