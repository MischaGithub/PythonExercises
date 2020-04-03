# Program for File Handling

#opening the selection.py file within a function

def read_file():
    with open("selection_sort.py") as my_file:
        return my_file.read()

#Calling the function and displaying the count of lines
def result_text():
        sample_output = read_file().splitlines()
        count = 0
        for line in sample_output:
            line = line.partition('#')[0]
            line = line.rstrip()
            if line.strip():
                count += 1
        return count

# Printing contents of selection_sort
print(read_file())
# Printing source code line's count
print("Total Number Of Lines Of Code:", result_text())