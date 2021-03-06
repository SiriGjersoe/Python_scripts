# Date: 6.3.20201
# Author: Siri Gjersøe

# This tiny script splits a string by a given charachter in a column of a csv file
# and writes an output file with new columns

from csv import reader
from csv import writer

# replace hypthen with comma - make an output doc with the new columns
with open('selection_exp_items.csv', 'r') as file, open('output_1.csv', 'w') as write_obj:
    csv_reader = reader(file)
    csv_writer = writer(write_obj)
# create new header row for the split columns
    csv_writer.writerow(['Column_1','Column_2','Column_3','Column_4','Column_5','Column_6','Column_7'])
    # split the first column with delimiter 'hyphen' into new columns and write a new file
    for column in csv_reader:
        new_column = column[0].split('-')
        column.append(new_column)
        csv_writer.writerow(new_column)
        print(new_column)
