import sys
import os
__description__ = 'Analyze File Extension'
__author__ = 'Osama Chaudhary'
__version__ = '0.0.1'
__date__ = '2018/07/14'
import optparse
def Main():
	oParser = optparse.OptionParser(usage='usage: %prog [options] [file]\n' + __description__, version='%prog ' + __version__)
	oParser.add_option('-d', '--data', action='store_true', default=False, help='Extract Highest Probability Extension')
	oParser.add_option('-l', '--loc', action='store_true', default=False, help='File Location')
	(options, args) = oParser.parse_args()
	l=len(args)
	if options.data:
		for i in range(l-1):
			#print str(i)+" : "+str(args[i])
			if args[i] == args[-1]:
				print("================================================================\nWORKING ON GETTING EXTENSION\n================================================================"),
				#extension type
				s=str(args[i+2]) #(.JAR)
				ext=s[1:len(s)-1] # .JAR
				print("Probability : "+args[i+1]+" | Extension : "+ext)
				print("================================================================\nRENAMING FILE\n================================================================"),
				#file new name
				print("Current :"+args[i]),
				name = args[i]
				name=name.replace("VirusShare_","MD5_")
				name=name+ext+''
				print("Renamed:"+name),
				os.rename(args[i],name)
				return 0
        return 0

if __name__ == '__main__':
	sys.exit(Main())
