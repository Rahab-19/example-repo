# Dictionary of flight prices by city (proper capitalization)
flight_prices = {
    "Los Angeles": 25000,
    "Shanghai": 18000,
    "Delhi": 32000,
    "Tokyo": 40000
}

# Calculate hotel price
def hotel_cost(num_nights):
    cost_per_night = 2500
    return num_nights * cost_per_night

# Calculate flight price
def plane_cost(city):
    return flight_prices.get(city, 0)

# Calculate car rental price
def car_rental(rental_days):
    cost_per_day = 780
    return rental_days * cost_per_day

# Calculate total holiday cost
def holiday_cost(num_nights, city, rental_days):
    return hotel_cost(num_nights) + plane_cost(city) + car_rental(rental_days)

# Show available destinations
print("Available cities: Los Angeles, Shanghai, Delhi, Tokyo")

# Collect user input
city = input("Enter the city you'll be flying to: ").title()
if city not in flight_prices:
    print("Sorry, we don't have flight cost info for that city.")
else:
    nights = int(input("How many nights will you stay at the hotel? "))
    days = int(input("How many days will you rent a car? "))

    # Calculate costs
    hotel = hotel_cost(nights)
    flight = plane_cost(city)
    car = car_rental(days)
    total = holiday_cost(nights, city, days)

    # Print cost breakdown
    print("\n--- Holiday Cost Breakdown ---")
    print(f"Destination City: {city}")
    print(f"Hotel Cost ({nights} nights): R{hotel:,}")
    print(f"Flight Cost: R{flight:,}")
    print(f"Car Rental Cost ({days} days): R{car:,}")
    print(f"Total Holiday Cost: R{total:,}")
