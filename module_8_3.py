class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


class Car:
    def __init__(self, model, vin, numbers):
        self.model = model  # название автомобиля (строка)
        if self.__is_valid_vin(vin):
            self.__vin = vin  # номер автомобиля (целое число)
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers  # номера автомобиля (строка)

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber("Incorrect type of VIN number.")
        elif vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinNumber("Incorrect range for VIN.")
        else:
            return True

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers("Incorrect datatype for the numbers.")
        elif len(numbers) != 6:
            raise IncorrectCarNumbers("Incorrect length of the numbers.")
        else:
            return True


# Everything is correct
try:
    car_1 = Car('Toyota', 2000000, 'SG5865')
except IncorrectVinNumber as e:
    print(e.message)
except IncorrectCarNumbers as t:
    print(t.message)
else:
    print(f'The car {car_1.model} is successfully created!')

# VIN is lower than needed
try:
    car_2 = Car('Honda', 20000, 'df2222')
except IncorrectVinNumber as e:
    print(e.message)
except IncorrectCarNumbers as t:
    print(t.message)
else:
    print(f'The car {car_2.model} is successfully created!')

# VIN is not int
try:
    car_3 = Car('BMW', '20000', 'df2222')
except IncorrectVinNumber as e:
    print(e.message)
except IncorrectCarNumbers as t:
    print(t.message)
else:
    print(f'The car {car_3.model} is successfully created!')

# Car number is shorter than expected
try:
    car_4 = Car('Mersedes', 2000000, 'SG5')
except IncorrectVinNumber as e:
    print(e.message)
except IncorrectCarNumbers as t:
    print(t.message)
else:
    print(f'The car {car_4.model} is successfully created!')

# Car number is not a string
try:
    car_5 = Car('Volkswagen', 2000000, 485955)
except IncorrectVinNumber as e:
    print(e.message)
except IncorrectCarNumbers as t:
    print(t.message)
else:
    print(f'The car {car_5.model} is successfully created!')
