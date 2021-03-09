# A simple function for extractingcolumns in a csv file
# and save them as a new csv file

import csv
# take a csv file as input in read mode, and an output file
# in write mode.
with open('Input_file.csv', 'r') as file, open('Output_file.csv', 'w+') as write_obj:
    file_csv = csv.reader(file)
    csv_writer = csv.writer(write_obj)
# loop through the csv input file
    for row in file_csv:
# save the content of the columns of intrest in a new variable.
        new_column = (row[2],row[5])
# write the new column to the output file
        csv_writer.writerow(new_column)
