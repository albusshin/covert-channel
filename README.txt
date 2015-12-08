Problem 1:
************

We implemented this covert channel communication by taking advantage of the shared file that we were provided with. The file lock status is checked to see if the bit transmitted is 0 or 1.

The algorithm is as follows.
Step 1: The sender starts with an given secret string. Get the shared file descriptor by opening the file.
Step 2: Keep polling the file lock status (using fcntl.flock method) from the sender to check if the receiver has started. Unlock it immediately.
Step 3: Start the Receiver, try constantly to lock the file until it acquires the lock.
Step 4: While polling, if the sender gets an IOError exception, it means that the receiver has acquired the lock, which means it has started.
Step 5: The sender and the receiver are synchronized.
Step 6: The sender starts the transmission of the secret string. Since the MSB of an ascii character is always zero, we do not transmit this bit. Only the remanining 7 bits of the character are sent. Hence 56 bits are sent in total. The sender sends a bit 1 by locking a file, and sends a bit 0 by unlocking the file.
Step 7: Concurrently, the receiver checks if the file is locked. If the file is locked, it means that the transmitted bit is 1. Else it is interpreted as a zero.
Step 9: The transmission is finished.

Problem 2:
************

This covert channel attack is implemented using similar method to what we used in problem 1, only we transmit the "Receiver started" message and the secret string using the CPU intensive operation finishing time instead of a file locking status.

The algorithm is as follows.
Step 1: The sender starts with an given secret string.
Step 2: In the sender, do 100 times of the CPU intensive operation, and establish a baseline for the running time of the operation.
Step 3: Then the sender waits for the receiver to start, by checking if the CPU intensive operation is running much longer than the baseline (with a factor of 1.7).
Step 4: The receiver is started. The receiver starts by first doing 10 seconds of CPU intensive operations.
Step 5: The sender knows the receiver has started. Then the sender sleeps for roughly 10 seconds to wait for the receiver finishes speaking.
Step 6: The receiver starts calculating the baseline for the CPU intensive calculation itself, for 5 seconds. At the same time, the sender waits for the receiver for 5 seconds before it starts transmission.
Step 7: The sender starts transmission. The sender sends a bit as 1 by doing 2 seconds of CPU intensive operations, and sends a bit as 0 by sleeping 2 seconds.
Step 8: The receiver receives a bit as 1 if the CPU intensive operation is running much longer than the baseline (with a factor of 1.3). The receiver receives a bit as 0 if the CPU intensive operation is running within the time of established baseline.
Step 9: The transmission is finished.
