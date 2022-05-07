#Function
def check_age (value):
    if value < 18:
        print('not an adult')
    else:
        print('is an adult')

age = 18
age2 = 17

check_age(age)
check_age(age2)