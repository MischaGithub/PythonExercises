#Sample Task program
#declaring the variables
my_file = open('sample task.txt', 'w+')
num_1 = int(input("Enter first number: \n"))
num_2 = int(input("Enter second number: \n"))
sum_num = num_1 + num_2
quotient = num_1 // num_2
diff_num = num_1 - num_2
product_num = num_1 * num_2
#displaying the desried results in the text file created
my_file.write(str(sum_num) + '\n')
my_file.write(str(quotient) + '\n')
my_file.write(str(diff_num) + '\n')
my_file.write(str(product_num) + '\n')
#closing the file
my_file.close()




