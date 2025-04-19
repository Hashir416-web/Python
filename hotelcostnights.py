def hotel_cost(nights):

    return nights * 140
def plane_ride(days):
    if days == "NYC":
        return 183
    elif days == "LA":
        return 220
    elif days == "ATX":
        return 222
    elif days == "Los Angeles":
        return 475
def rental_car(days):
    if days <= 7:
        return days * 40-50
    elif days > 3:
        return (days * 40) - 20
    else:
        return (days * 40)
def trip_cost(city, days, spending_money):
    return hotel_cost(days) + plane_ride(city) + rental_car(days)+spending_money
print("cost of rental car: ", rental_car(5))
print("cost of `plane ride`: ", plane_ride("NYC"))
print("cost of hotel ride: ", hotel_cost(7))
print ("cost of trip: ", trip_cost("NYC", 5, 600))
print(trip_cost("Los Angeles", 3, 200))