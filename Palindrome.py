#A Recursive Program
#check if str is a palindrome or not
#Reference GeeksforGeeks

def is_pal_rec(st, s, e):
    # if there is only one character
    if s == e:
        return True

    #if the first and last character do not match
    if st[s] != st[e]:
        return False

    if s < e + 1:
        return is_pal_rec(st, s + 1, e - 1)


#An empty string is considered as a palidrome
def is_palindrome(st):
    n = len(st)

    if n == 0:
        return True
    return is_pal_rec(st, 0, n - 1)

#Check whether the user input is Palidrome

user_input = str(input("Enter a Palidrome phrase: \n"))
if is_palindrome(user_input):
    print("Yes it is", is_palindrome(user_input))
else:
    print("No it is not", is_palindrome(user_input))




