import fcntl
import time
import sys

timeInterval = 0.2

def lockFile():
    fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)  #Try to acquire file lock
def unlockFile():
    fcntl.flock(fd, fcntl.LOCK_UN)  #Unlock file

secret = sys.argv[1]
print "Secret is: ", secret

f = open("sharedfile", "r")
fd = f.fileno()
print fd
while True:
    try:
        lockFile()
    except IOError:
        print "foo2"
        break
    unlockFile()

#time.sleep(timeInterval)

def transmit(b):
    print "Transmitting", b
    if bit == 0:
        unlockFile()
    else:
        lockFile()

for c in secret:
    byte = ord(c)
    for i in range(0, 7):
        bit = byte & (1 << (6 - i))
        print bit
        transmit(bit)
        time.sleep(timeInterval)

