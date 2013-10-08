# Defines cars with the value of 100
cars = 100
# Defines space_in_a_car with the value of 4.0 (Floating point)
space_in_a_car = 4.0
# Defines drivers with the value of 30
drivers = 30
# Defines passengers with the value of 90
passengers = 90
# Defines car_not_driven as the value of cars subtracted by drivers
cars_not_driven = cars - drivers
# Defines cars_driven with the same value of drivers
cars_driven = drivers
# Defines carpool_capacity as the value of cars_driven multiplied by space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
# Defines average_passengers_per_car as the value of passengers divided by cars_driven
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."