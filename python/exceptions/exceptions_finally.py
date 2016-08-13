import sys,time
f=None
try:
	f=open("poem.txt")
	while True:
		line=f.readline()
		if len(line) == 0:
			break
		print line,
		sys.stdout.flush()
		time.sleep(2)
except IOError:
	print "file not exists"
except KeyboardInterrupt:
	print "cancelled the reading from file"
finally:
	if f:
		f.close()
	print "cleaning up, close the file"
