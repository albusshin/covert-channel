#!/usr/bin/python

import time
import sys
import math

timeInterval = 1

def operation():
    for i in range (0, 100000):
        math.sqrt(2)

baseline = 0
print >> sys.stderr,  'establishing baseline...'
for i in range (0, 100):
    start = time.time()
    operation()
    interval = time.time() - start
    baseline += interval

baseline /= 100
threshold = baseline * 2

print >> sys.stderr,  'baseline: ', baseline
print >> sys.stderr,  'threshold', threshold

def otherRunning():
    start = time.time()
    operation()
    interval = time.time() - start
    if interval > threshold:
        return True
    else:
        return False

secret = sys.argv[1]
print >> sys.stderr,  "Sending", secret

while not otherRunning():
    pass

print >> sys.stderr,  "receiver is running"
print >> sys.stderr,  "waiting for receiver's establishing baseline"
time.sleep(2)

print >> sys.stderr,  "start transmission"

def transmit(b):
    start = time.time()
    if b != 0:
        print >> sys.stderr,  'transmitting 1'
        while time.time() - start < timeInterval:
            operation()
    else:
        print >> sys.stderr,  'transmitting 0'
        time.sleep(timeInterval - (time.time() - start))

for c in secret:
    byte = ord(c)
    for i in range(0, 7):
        started = time.time()
        bit = byte & (1 << (6 - i))
        transmit(bit)
