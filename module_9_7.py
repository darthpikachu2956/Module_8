def is_prime(fun):
    def wrapper(*args):
        number = fun(*args)
        if number < 2:
            return False
        for i in range(2, number):
            if number % i == 0:
                return 'Составное'
        return 'Простое'
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result_1 = sum_three(1, 0, 0)
print(result_1)
result_2 = sum_three(1, 2, 7)
print(result_2)
result_3 = sum_three(1, 2, 0)
print(result_3)
