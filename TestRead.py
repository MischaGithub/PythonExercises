file = open('testread.txt', 'r')
my_file = file.readlines()

new_list = []
for line in my_file:
    new_list.append(line.strip())

print(new_list)
