import sys
import subprocess

if sys.argv == None or len(sys.argv)!= 3:
	sys.exit()
n = int(sys.argv[1])
m = int(sys.argv[2])

f= open("distribution.txt","w+")
make = ["python","distribution.py",str(n)]
init = ["./set_client",str(n),"<","distribution.txt"]
get = ["./get_client",str(n),"<","distribution.txt"]

subprocess.call(make,stdout=f)
# subprocess.call(init)
# subprocess.call(get)