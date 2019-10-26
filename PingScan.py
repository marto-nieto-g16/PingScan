#!/usr/bin/env python
from subprocess import Popen, PIPE
cont = 0
print "PingScan: Buscando Dispositivos"
print " "
for ip in range(50,150):
	ipAddress = '192.168.1.'+str(ip)
	subprocess = Popen(['/bin/ping', '-c 1 ', ipAddress], stdin=PIPE, stdout=PIPE, stderr=PIPE)
	stdout, stderr= subprocess.communicate(input=None)
	if "bytes from " in stdout:
		cont +=1
		print "| "+str(cont)+" | %s | IP Activa |" %(stdout.split()[1])
		with open("ips.txt", "a") as myfile:
			myfile.write(stdout.split()[1]+'\n')
print "Total De Dispositivos Activos: " + str(cont)
