def hotel_cost(nights):
    return 140*nights

def plane_ride_cost(city):
    if "Charlotte" == city:
        return 183
    elif "Tampa" == city:
        return 220
    elif "pittburgh" == city:
        return 222
    elif "Los Angeles" == city:
        return 475

def rental_car_cost(days):
    if days>= 7 :
        return 4*days - 50
    elif days>=3 :
        return 40*days - 20
    else:
        return 40*days

def trip