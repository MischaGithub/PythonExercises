#DECLARING THE VARIABLES IN THE PROGRAM
av_speed = int(input("Enter the average allowable speed \n"))
demerits = 1
current_speed = float(input("Enter speed detected \n"))

#Creating a loop in order for the demerits point to by calculated according to the formula below
if av_speed >= current_speed:
    print("OK")
elif av_speed < current_speed:
    demerits = (current_speed-av_speed)/5
    print(int(demerits), "points")
    if demerits >= 12:
        print(int(demerits), "Time to go to JAIL!")



