import fcntl
import time

timeInterval = 0.2
l = []

def lockFile():
    fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)  #Try to acquire file lock
def unlockFile():
    fcntl.flock(fd, fcntl.LOCK_UN)  #Unlock file

f = open("sharedfile", "r")
fd = f.fileno()
print fd
while True:
    try:
        lockFile()
        break
    except IOError:
        pass

unlockFile()
#time.sleep(timeInterval)
time.sleep(timeInterval / 2)

def receive():
    b = 0
    try:
        lockFile()
        b = 0
    except IOError:
        b = 1
    unlockFile()
    print "Receiving", b
    l.append(b)

for i in range (0, 56):
    receive()
    time.sleep(timeInterval)

print l
