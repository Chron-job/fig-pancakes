#!/usr/bin/python
# 
# Chris Newton 
# V 1.1
# Take input from fierce DNS scan and ouput excel file
# Usage fierce_parser.py -i <input filename> -o <output filename>
# If no output file is specified, the input filename will be used by default

import sys, getopt, xlwt, os

def main(argv):
# Variables	
	inputfile = ' '
	outputfile = ' '
	book = xlwt.Workbook()
	sh = book.add_sheet("Sheet1")
	n = 0
	
# Verify input parameters
	if len(sys.argv) < 2:
		print 'fierce_parser.py -i <inputfile> -o <outputfile>'
		sys.exit(2)
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
	if outputfile == ' ':
		outputfile = inputfile + ".xlsx"

# Read input file into list		
	file = open(inputfile, 'r')
	lines = file.readlines()
	file.close()

# Write list to file	
	for line in lines:
		if line[0].isdigit():
			domain = line.split( )
			sh.write(n,0,domain[0])
			sh.write(n,1,domain[1])
			n = n+1

# Save file and print confirmation			
	if outputfile.endswith(".xlsx"):
		book.save(outputfile)
		print "New file: " + os.getcwd() + "/" + outputfile
	else:
		book.save(outputfile + ".xlsx")
		print "New file: " + os.getcwd() + "/" + outputfile + ".xlsx"
	
if __name__ == "__main__":
	main(sys.argv[1:])
	