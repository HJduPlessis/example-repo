def hotel_cost(nights):
    return nights*50;

def plane_cost(location):
    if (location=='london'):
        return 12000;
    elif (location=='paris'):
        return 13000;
    elif (location=='rome'):
        return 11000;
    else:
        print('Flight information not found. Restart and enter new destination.');
        return 0;

def car_rental(renting):
    return renting*75;

def holiday_cost(flight,hotel,car):
    costs=[];
    on_holiday=plane_cost(flight);
    costs.append(on_holiday);
    if (on_holiday!=0):
        costs.append(hotel_cost(hotel));
        on_holiday+=costs[1];
        costs.append(car_rental(car));
        on_holiday+=costs[2];
    else:
        costs.append(0);
        costs.append(0);
    costs.append(on_holiday);
    return costs;

city_flight=input("Where are you traveling to (London/Paris/Rome): ").lower();
num_nights=int(input("How many nights will you be staying: "));
rental_days=int(input("How many days will you be renting a car for: "));

trip_budget=holiday_cost(city_flight,num_nights,rental_days);
print(f'Cost of flight to {city_flight}: {trip_budget[0]}');
print(f'Cost of {num_nights} night hotel stay: {trip_budget[1]}');
print(f'Cost of {rental_days} day car rental: {trip_budget[2]}');
print(f'Total cost of holiday: {trip_budget[3]}');