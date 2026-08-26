# Write a script to count the number of lines in a file.

file_name = "files.py"

with open(file_name, "r") as file:
    line_count = 0

    for line in file:
        line_count += 1

print("Total lines:", line_count)