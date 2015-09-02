from subprocess import Popen, PIPE, call
from random import uniform
from sys import argv,exit
import os

tests={"printrandom":2,"temperatureconverter":3,"linecounter":3,"wordcounter":2}
total=10
def run_tests(random,temp,lines,words,a):
	tr=test_random() if random else 2
	if tr==0:
		print "\nPassed"
		print "-"*20
	tt=test_temp() if temp else 2
	if tt==0:
		print "\nPassed"
		print "-"*20
	tl=test_lines() if lines else 2
	if tl==0:
		print "\nPassed"
		print "-"*20
	elif tl==1:
		tests["linecounter"]=0
	tw=test_words() if words else 2
	if tw==0:
		print "\nPassed"
		print "-"*20
	elif tw==1:
		tests["wordcounter"]=0

	if a:
		count=0
		print "\nTOTAL\n"
		for t in tests:
			count+=tests[t]
			print "{0}: {1} pts".format(t,tests[t])

		print "-"*20
		print "Total {0}/{1}".format(count,total)


def test_random():
	print "\nPrint random\n"
	for i in range(1,10):
		process = Popen(["python", "printrandom.py"], stdout=PIPE)
		out = float(process.communicate()[0])
		fnr=len(str(out).replace('-',''))
		print out
		if out>1 or out<-1 or fnr>6:
			print "Failed at {0}".format(out)
			tests["printrandom"]=0
			return 1
	return 0

def test_temp():
	print "\nTemperature convert\n"
	for x in range(10):
		i=uniform(-100,200)
		process = Popen(["python", "temperatureconverter.py",str(i)], stdout=PIPE)
		out = process.communicate()[0].lower()
		print out.strip()
		words=out.split()
		celsius="{0:.1f}".format((i-32)/1.8)
		if words.count(celsius)==0 or words.index(celsius)<2:
			print "Failed at "+out
			tests["temperatureconverter"]=0
			return 1
	return 0

args=['testfile1.txt','testfile2.txt','testfile3.txt']
def test_lines():
	print "\nLine count\n"
	file1 = open(args[0], 'w+')
	file1.write("This file has 2 lines and \n 8 words")
	file2 = open(args[1], 'w+')
	file2.write("This file has 3 lines and \n 10 words \n in it")
	file3 = open(args[2], 'w+')
	file3.write("This file has 1 line")
	file1.close()
	file2.close()
	file3.close()
	process = Popen(["python", "linecounter.py",args[0],args[1],args[2]], stdout=PIPE)
	out = process.communicate()[0].lower().replace(':',': ').split('\n')
	print "\n".join(out).strip()
	if 'testfile1.txt' not in out[0].split() and '2' not in out[0].split():
		print "Failed at "+out[0]
		return 1
	elif 'testfile2.txt' not in out[1].split() and '3' not in out[1].split():
		print "Failed at "+out[1]
		return 1
	elif 'testfile3.txt' not in out[2].split() and '1' not in out[2].split():
		print "Failed at "+out[2]
		return 1
	return 0


def test_words():
	print "\nWord count\n"
	process = Popen(["python", "wordcounter.py",args[0],args[1],args[2]], stdout=PIPE)
	out = process.communicate()[0].lower().split('\n')
	print "\n".join(out).strip()
	for x in args:
		os.remove(x)
	if 'testfile1.txt' not in out[0].split() and '8' not in out[0].split():
		print "Failed at "+out[0]
		return 1
	elif 'testfile2.txt' not in out[1].split() and '10' not in out[1].split():
		print "Failed at "+out[1]
		return 1
	elif 'testfile3.txt' not in out[2].split() and '5' not in out[2].split():
		print "Failed at "+out[2]
		return 1
	return 0

r=False
t=False
l=False
w=False
v=True
a=False
for x in argv[1:]:
	if "printrandom" in x:
		r=True
	elif "temperatureconverter" in x:
		t=True
	elif "linecounter" in x:
		l=True
	elif "wordcounter" in x:
		w=True
	elif "all" in x:
		r=True
		t=True
		l=True
		w=True
		a=True
	else:
		print "Not valid"
		v=False

if len(argv)==1:
	r=True
	t=True
	l=True
	w=True
	a=True

run_tests(r,t,l,w,a) if v else exit