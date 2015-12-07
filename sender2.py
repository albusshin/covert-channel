#!/usr/bin/python

import time
import sys
import math

timeInterval = 2

def operation():
    for i in range (0, 100000):
        math.sqrt(2)

baseline = 0
print 'establishing baseline...'
for i in range (0, 1000):
    start = time.time()
    operation()
    interval = time.time() - start
    baseline += interval

baseline /= 1000
print 'baseline: ', baseline

def otherRunning():
    start = time.time()
    operation()
    interval = time.time() - start
    if interval > baseline * 1.5:
        return True
    else:
        return False

secret = sys.argv[1]

while not otherRunning():
    pass

print "other running"

time.sleep(baseline * 1000)

print "start transmission"

def transmit(b):
    start = time.time()
    if b != 0:
        print 'transmitting 1'
        while time.time() - start < timeInterval:
            operation()
    else:
        print 'transmitting 0'
        time.sleep(timeInterval - (time.time() - start))

for c in secret:
    byte = ord(c)
    for i in range(0, 7):
        started = time.time()
        bit = byte & (1 << (6 - i))
        transmit(bit)
