def add_everything_up(a, b):  # adds numbers and strings
    try:
        return a + b
    except TypeError:
        c = str(a) + str(b)
        return c


print(add_everything_up(15, 2.5))
print(add_everything_up(1, 'lalala'))
print(add_everything_up('apple', 12.3))
