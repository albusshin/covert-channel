#!/usr/bin/python

import fcntl
import time
import sys

timeInterval = 0.3

def lockFile():
    fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)  #Try to acquire file lock
def unlockFile():
    fcntl.flock(fd, fcntl.LOCK_UN)  #Unlock file

secret = sys.argv[1]

f = open("shared_file", "r")
fd = f.fileno()

while True:
    try:
        lockFile()
    except IOError:
        break
    unlockFile()

time.sleep(timeInterval)

def transmit(b):
    if b != 0:
        #print 'transmitting 1'
        lockFile()
    else:
        #print 'transmitting 0'
        unlockFile()

for c in secret:
    byte = ord(c)
    for i in range(0, 7):
        started = time.time()
        bit = byte & (1 << (6 - i))
        transmit(bit)
        now = time.time()
        time.sleep(timeInterval - (now - started))
