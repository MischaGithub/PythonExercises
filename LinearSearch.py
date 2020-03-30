#Program to perfom linear search

def linear_search(my_letters, key_letter):
    letter2 = []
    dup_letter = False
    for i in range(len(my_letters)):
        if key_letter == my_letters[i]:
            return i
    return None


my_letters = ["C", "A", "N", "D", "I", "C", "E"]
key_letter = "D"
print("key letter is found at index  " + str(linear_search(my_letters, key_letter)))
