Problem 1:
************

We implemented this covert channel communication by taking advantage of the
shared file that we were  provided with. The file lock status is checked to see if the bit transmitted is 0 or 1.

The algorithm is as follows.
Step 1: Start Sender, lock the shared file and get its file descriptor. Unlock it.
Step 2: Keep polling the file from the sender.py to check if the receiver had started. Unlock it immediately.
Step 2: Start Receiver, lock the file. 
Step 3: While polling, if the sender gets an IOError exception, it means that the receiver has started.
Step 4: Start transmission of the received string. Since the MSB of an ascii character is always zero, we do not transmit this bit. Only the remanining 7 bits of the character are sent. Hence 56 bits are sent in total.
Step 5: Concurrently, the receiver checks if the file is locked. If the file is locked, it means that the transmitted bit is 1. Else it is interpreted as a zero.
