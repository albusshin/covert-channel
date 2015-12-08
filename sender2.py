#!/usr/bin/python

import time
import sys
import math

timeInterval = 2

def operation():
    for i in range (0, 100000):
        math.sqrt(2)

baseline = 0
for i in range (0, 100):
    start = time.time()
    operation()
    interval = time.time() - start
    baseline += interval

baseline /= 100
threshold = baseline * 1.5


def otherRunning():
    aggregated = 0
    for i in range(0, 10):
        start = time.time()
        operation()
        aggregated +=  time.time() - start
    if aggregated / 10 > threshold:
        return True
    else:
        return False

secret = sys.argv[1]

while not otherRunning():
    pass
time.sleep(9.5)

time.sleep(5.0)


def transmit(b):
    start = time.time()
    if b != 0:
        while time.time() - start < timeInterval: operation()
    else:
        time.sleep(timeInterval - (time.time() - start))

for c in secret:
    byte = ord(c)
    for i in range(0, 7):
        started = time.time()
        bit = byte & (1 << (6 - i))
        transmit(bit)
