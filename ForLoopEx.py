#Program for loops
cars = ["BMW", "VW", "FORD", "NISSAN", "HONDA", "SUZUKI"]
bikes = ["HARLEY", "SUZUKI","YAMAHA", "HONDA ACTIVA", "KTM RC"]
#Creating the for loop
for thecars in cars:
    for thebikes in bikes:
        #Nested loop
        print(thecars, thebikes)
        #telling the program to stop with BREAK
        #Creating a loop to print what is in the range
        for number in range(1, 11):
            print(number)
            for numbers in range(2, 21, 2):
                print(numbers)
             #ending the loop and print the text
            else :
                print("we have finished the topic on loops")






