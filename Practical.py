str_country = "????South Africa????"

#creating a loop
with open ("selection_sort.py", "r") as infile:
    #having a nested loop
    with open("newsample.txt", "w+") as outfile:
        #print the selection.py files in the text file
        for lines in infile:
            outfile.write(lines)

import os

os.remove("newsample.txt")





