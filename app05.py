#List
cars = ['bmw', 'tesla', 'mercedes']
print(cars)
print('Size of the list:' + str(len(cars)))

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.capitalize())
