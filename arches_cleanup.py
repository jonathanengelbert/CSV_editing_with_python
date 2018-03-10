#============================================================
#               ARCHES CSV CLEANUP
#            LAST MODIFIED: 03/08/2018
#            AUTHOR: Jonathan Engelbert
#============================================================

#DESCRIPTION: This script cleans up csv files generated by a Arches Process. It generates e a new csv file mirroring all data, while extracting picture file names from field column "Information Carrier", and printing them separated by commas, enclosed in double quotes.

import re
import csv


#READER

input = open("input.csv", "rb")
reader = csv.reader(input)

#WRITER

output = open('output.csv', 'wb')
writer = csv.writer(output)

# ITERATION AND LOGIC

for row in reader:
    match = re.findall("u'name':\su'(.+?(?='))", row[1])
    if match:
        match = str(match)
        drop_single_quotes = re.sub("'", "", match)


        #Replaces both brackets with double quotes
        left_bracket = drop_single_quotes.replace('[', '"')
        right_bracket = left_bracket.replace(']', '"')
        #Removes White space
        final = right_bracket.replace(" ","")
        row[1] = final


#WRITE TO OUPUT
    writer.writerow(row)

input.close()
output.close()



