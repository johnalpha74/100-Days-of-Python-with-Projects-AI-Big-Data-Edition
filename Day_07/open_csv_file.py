# read a .csv file in Python and print each row, using open()

# import the csv module

import csv

# csv opening and reading
def print_csv_rows(file_path):
    with open(file_path, mode="r") as file:  # with open(...): Automatically closes the file after the block.
        reader = csv.reader(file)
        for row in reader:  # csv.reader: Reads each row as a list of strings.
            print(row)


# call the function
print_csv_rows('my_csv_file.csv')
