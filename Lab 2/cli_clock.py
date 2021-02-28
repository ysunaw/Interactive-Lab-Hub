from time import strftime, sleep
import os
while True:
    text = strftime("%m/%d/%Y %H:%M:%S") # , end="", flush=True)
    cmd = "echo {}".format(text)
	os.system(cmd)
    # print("\r", end="", flush=True)
    # sleep(1)
