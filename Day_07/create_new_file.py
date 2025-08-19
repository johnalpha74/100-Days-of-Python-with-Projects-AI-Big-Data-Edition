# Write a program to create a new file and add contents from an existing file

with open("C:\\users\\user\\canada_figures.txt", "r") as file:
    with open("C:\\users\\user\\new_canada_figures.txt", "w") as file_out:

        # Open the input file for reading
        for line in file:
            tokens = line.split(' ')
            file_out.write("Wordcount is " + str(len(tokens)) + " words: " + line)

file.close()
file_out.close()

