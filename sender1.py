#!/usr/bin/python

import fcntl
import time
import sys

timeInterval = 0.2

def printerr(s):
    print >> sys.stderr, s
def lockFile():
    fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)  #Try to acquire file lock
def unlockFile():
    fcntl.flock(fd, fcntl.LOCK_UN)  #Unlock file

secret = sys.argv[1]
print >> sys.stderr, "Sending:", secret

f = open("shared_file", "r")
fd = f.fileno()
while True:
    try:
        lockFile()
    except IOError:
        break
    unlockFile()

def transmit(b):
    printerr('transmitting ' + `b`)
    if bit == 0:
        unlockFile()
    else:
        lockFile()

for c in secret:
    byte = ord(c)
    for i in range(0, 7):
        started = time.time()
        bit = byte & (1 << (6 - i))
        transmit(bit)
        now = time.time()
        time.sleep(timeInterval - (now - started))
