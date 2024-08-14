def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_data += 1
            print(f'Incorrect type of data for calculating the amount: {i}')
    return result, incorrect_data


def calculate_average(numbers):
    average = None
    try:
        result, incorrect_data = personal_sum(numbers)
        valid = len(numbers) - incorrect_data
        average = result / valid if valid > 0 else 0
    except ZeroDivisionError:
        average = 0
    finally:
        return f'{average}\n'


print(f'Result 1: {calculate_average("1, 2, 3")}')
print(f'Result 2: {calculate_average([1, "String", 3, "Another"])}')
print(f'Result 3: {calculate_average(567)}')
print(f'Result 4: {calculate_average([42, 15, 36, 13])}')
