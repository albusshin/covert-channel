#!/usr/bin/python

import fcntl
import time
import sys

timeInterval = 0.2
l = []

def printerr(s):
    print >> sys.stderr, s
def lockFile():
    fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)  #Try to acquire file lock
def unlockFile():
    fcntl.flock(fd, fcntl.LOCK_UN)  #Unlock file

f = open("shared_file", "r")
fd = f.fileno()
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
    printerr("receiving " +  `b`)
    l.append(b)

for i in range (0, 56):
    started = time.time()
    receive()
    now = time.time()
    time.sleep(timeInterval - (now - started))

def bitArray2String(arrBits):
    strResult = [];
    # To DO:
    # 1. Insert a leading zero
    # 2.  convert every 8 bits into an integer
    # 3. Obttain characters from the integers
    # 4. Concatenate the characters into a string

    # Inserting leading Zeros
    for i in range(0,8):
        if(i==0):
        
            arrBits.insert(i,0)
    
        
        else:
            arrBits.insert((i*7)+i,0)
    
    #print(arrBits); 
    
    #2 convert every 8 bits into integer
    arrIntegers = [];
    result = 0;
    for i in range(0,8):
        char = arrBits[i*8:(i+1)*8];#char has the 8 bits required
        shiftIndex = 7;
        for j in char:
            result = result | j<<shiftIndex;
            shiftIndex = shiftIndex-1;
        arrIntegers.append(result);
        result = 0;

    #print(arrIntegers);

    #3. Obtain characters from the string
    arrChar = [];
    
    for i in arrIntegers:
        arrChar.append(chr(i));

    #4. Concatenaate
    print(''.join(arrChar));
    print >> sys.stderr, "Receiving", ''.join(arrChar)

bitArray2String(l)
