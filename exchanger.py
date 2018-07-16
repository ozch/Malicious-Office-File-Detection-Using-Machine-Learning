import os
class Exchanger:
	MAIN_DIR = None #Main Directory for output
	OUT_DIR = None
	CUR_FILE = None	
	def __init__(self,DIR=None):
		if DIR == None:
			return
		self.MAIN_DIR = DIR

	def setOutDir(self):
		directory =str(self.MAIN_DIR)+str(self.CUR_FILE)
		if not os.path.exists(directory):
			os.makedirs(directory)
		self.OUT_DIR= directory
	def getOutDir(self):
		self.setOutDir()
		return self.OUT_DIR

	def setFileName(self,fname):
		self.CUR_FILE=fname
	def getFileName(self):
		return self.CUR_FILE
#import os
#if not os.path.exists(directory):
#    os.makedirs(directory)
