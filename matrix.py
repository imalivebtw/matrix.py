import time as t
import sys
import random as r

phrase = "this is an example text"

for char in list(phrase):
    time = r.randint(1, 5)/10
    t.sleep(time)
    sys.stdout.write(char)
    sys.stdout.flush()
print("")

