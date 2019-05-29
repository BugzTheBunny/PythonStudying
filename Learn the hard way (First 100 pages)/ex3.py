cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passenger_per_car = passengers / cars_driven

print("Ther are ", cars , " Cars available.")
print("There are only ", drivers, " drivers available.")
print("There will be ", cars_not_driven, " empty cars today.")
print("We can transport ",carpool_capacity, " people today.")
print("We have ", passengers, " to carpool today")
print("We need to put about ", average_passenger_per_car, " in each car.")

#The error from the book is because of the fact that the 
#variable the author wrote is "car_pool_capacity", while the right name is "carpool_capacity".

# 1 - no, its not necessary, python casts the int to float.

