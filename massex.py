#!/usr/bin/env python
import subprocess
import copy
import time
import os
from exchanger import *
MAIN_DIR = "./feed/"
OUT_DIR = "./output/"
ex=Exchanger(OUT_DIR)
def getList():
	if os.path.exists(MAIN_DIR):
		files = subprocess.Popen('ls '+MAIN_DIR, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	else:	
		print("Please make sure your directory has a name like './feed/' starting with '.'")
		print("Existing Program in 3 Seconds")
		time.sleep(3)	
		exit()
	return files
def printList():
	files = getList()
	print("List of files to be processed in ./test dir")
	for line in files.stdout.readlines():
		print("::"+line)

def getMeta():
	files = subprocess.Popen('ls '+MAIN_DIR+'', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	return files
def getCommand(a,b):
	fu ="python oledump.py {0} --dir {1}".format(a,b)
	return fu

print("\nStarting Process...\n")
w_file = getList()
for file in w_file.stdout.readlines():
	f_name= MAIN_DIR+file.decode('utf-8')
	print ("===================================================\n===================================================")	
	print("File Under Processing : "+file.decode('utf-8')) 
	ex.setFileName(file.decode('utf-8'))
	print("Input Location : "+f_name)
	print("Output Dir for Data : "+ex.getOutDir())
	st = getCommand(f_name,ex.OUT_DIR)
	print('Command::Get File VBA & OLE \n' + st)
	print("---------------------------------------------------\n")
	dump = files = subprocess.Popen("python oledump.py ./feed/docm.docm --dir ./output/docx.docx", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	for d in dump.stdout.readlines():
		print(" \t "+d.decode('utf-8'))
	
