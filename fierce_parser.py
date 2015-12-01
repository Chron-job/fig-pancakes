#!/usr/bin/python
# Take input from fierce DNS scan and ouput excel file
# Usage fierce_parser.py -i <input filename> -o <output filename>

import sys, getopt, xlwt

def main(argv):
#Variables	
	inputfile = ' '
	outputfile = ' '
	book = xlwt.Workbook()
	sh = book.add_sheet("Sheet1")
	n = 0
	
	try:
		opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print 'fierce_parser.py -i <inputfile> -o <outputfile>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'fierce_parser.py -i <inputfile> -o <outputfile>'
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg
	file = open(inputfile, 'r')
	lines = file.readlines()
	file.close()
	for line in lines:
		if line[0].isdigit():
			domain = line.split( )
			sh.write(n,0,domain[0])
			sh.write(n,1,domain[1])
			n = n+1
	book.save(outputfile)
	print "File output: " + outputfile
if __name__ == "__main__":
	main(sys.argv[1:])
	