import subprocess

subprocess.Popen('date +%T -s "13:37:00"', stdin = subprocess.PIPE, stdout = subprocess.PIPE)
while(1):
	sp = subprocess.Popen('./potential', stdin = subprocess.PIPE, stdout = subprocess.PIPE)
	print str(sp.pid)
	if sp.pid == 1337:
		print "OMG"
		print sp.communicate(input="217552398261569-545326772-1082328767-1082328760-1082328765-1082328753")
		exit()
	
