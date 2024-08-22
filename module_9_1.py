def apply_all_func(int_list, *functions):
    results = {}
    for i in functions:
        x = i(int_list)
        results[i.__name__] = x
    return results


print(apply_all_func([1, 5, 7, 3, 2], max, min))
print(apply_all_func([1, 5, 7, 3, 2], len, sum, sorted))
