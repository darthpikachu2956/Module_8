def all_variants(text):
    n = len(text)
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            yield text[i:i + length]


a = all_variants("Sberbank")
for j in a:
    print(j)
