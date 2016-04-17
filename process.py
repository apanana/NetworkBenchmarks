import sys
import subprocess

if sys.argv == None or len(sys.argv)!= 3:
	sys.exit()
n = int(sys.argv[1])
m = int(sys.argv[2])

make = ["python","distribution.py",str(n),">","distribution.txt"]
init = ["distribution.txt",">","./set_client",str(n)]
get = ["distribution.txt",">","./get_client",str(n)]

subprocess.call(make)
subprocess.call(init)
subprocess.call(get)