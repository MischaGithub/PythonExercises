def hotel_cost(nights):
    #Calculating the hotel cost per stay
    hotel_cost = nights * 140
    return hotel_cost

def plane_ride_cost(city):
    #Calculating the plane ride cost depending on location

    if city == "Cape Town":
        return 2500
    if city == "Durban":
        return 2300
    if city == "JHB":
        return 2000
    if city == "BFN":
        return "Sorry select only FLIGHTS between Cape Town, Durban, JHB"


def rental_car_cost(days):
    #Calculating the cost per day for the rental car
    cost = days * 40
    if days >= 7:
        cost -= 50
        return "Cost to rent car:" + str(cost)
    elif days >= 3 and days <= 6:
        cost -= 20
        return cost

def trip_cost(city, days, spending_money):
    #Calculating the trip cost with all its attributes
    return hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days) + spending_money

Hotel_charge = int(input("Enter nights to stay: \n"))
print("This is the cost to stay in hotel: ", hotel_cost(Hotel_charge))
Plane_cost = str(input("Enter the city you travelling to: \n"))
print("The plane ride cost is:",plane_ride_cost(Plane_cost))
Daily_rental = int(input("Enter days required for rental car: \n"))
print("Daily cost for rental car is:", rental_car_cost(Daily_rental))


















