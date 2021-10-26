# cmd command: python demo35.py -a -b -c

import sys
import os
import time

print(sys.executable)
print(os.getcwd())
print(sys.argv)
directory = "data"
os.mkdir(directory)
os.chdir(directory)
print(os.getcwd())
time.sleep(10)
os.chdir("..")
os.rmdir(directory)
