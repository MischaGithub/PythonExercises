#Declaring the functions need to do add,subtract, multipy and divide


#declaring the addition to be done
def simple_add():
    add_answer = first_num + second_num
    print("Sum of the numbers is:")
    return add_answer

#declaring the function of  substration
def simple_sub():
    sub_answer = first_num - second_num
    print("Subtraction of the numbers is:")
    return sub_answer

#declaring the multiplication of the two number
def simple_multiply():
    mul_answer = first_num * second_num
    print("The mutiplication of the two number is:")
    return mul_answer

#declaring the division of the two numubers
def simple_div():
    div_answer = first_num / second_num
    print("The Division of the to numbers is:")
    return div_answer

#print each of methods
first_num = int(input("Enter the first number: \n"))
second_num = int(input("Enter the second number: \n"))
print(simple_add())
print(simple_sub())
print(simple_multiply())
print(simple_div())

















