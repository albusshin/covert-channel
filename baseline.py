#!/usr/bin/python

import time
import math

def operation():
    for i in range (0, 10000000):
        math.sqrt(2)
while True:
    start = time.time()
    operation()
    interval = time.time() - start
    print interval

