import csv
import itertools

'''Set up how to read the file. 
Choose the range of the rows in the parentheses.
Remember: with an index, you have to subtract 1'''

#add itertools.islice to print entire file with row restrictions

with open('Combined_Export_File.csv') as csvfile:
	readCSV = csv.reader(csvfile, dialect='excel')
#choose the columns that are printed. remember indexes!
	for column in readCSV:
		if "SLEEP" in column: #limit the printing to sleep, does not print the headers
			print (column)
