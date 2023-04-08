# CSV File
""" csv (comma seperated values) is a simple file format
 used to store tabular data, such as a spreadsheet or database.
 a csv file stores tabular data (numbers and text) in plain text."""

import csv

fields = ["name", "branch", "year", "CGPA"]

rows = [ ['Harry', 'CE', '2', '9.0'],
        ['Joy', 'CSE', '3', '9.5'],
        ['Ahana', 'ME', '3', '9.7'],
        ['Tom', 'EE', '2', '8.7'],
        ['Bella', 'EC', '3', '9.6']]

filename = "college_record.csv"

with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(fields)

    csvwriter.writerows(rows)

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)