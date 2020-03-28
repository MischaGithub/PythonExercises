#Pogram for sorting the list with the selction sort methond
#this was an introduction to selection sort

pet_names = ["Danny Boy", "Georgy Girl", "Satchi", "Bullet", "Miss Daisy", "Guffy", "Lady", "Tinky", "Eleonor",
            "Tiger", "Master", "Abigail", "Queen", "Trevor", "Snuffels"]

#creating the function to do the selection sort

def Pet_Names(pet_names):
    for i in range(0, len(pet_names)):
        min_index = i
        for j in range (i+1, len(pet_names)):
            if pet_names[min_index] > pet_names[j]:
                min_index = j

        pet_names[i], pet_names[min_index] = pet_names[min_index], pet_names[i]


#Displaying the result for the selection sorting
print("Sorted array")
for i in range(len(pet_names)):
    print("Pet Name:", str(pet_names[i]))








