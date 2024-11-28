
def generate_password(n):
    pairs = []
    for i in range(1, n):
        for m in range(i + 1, n):
            if n % (i + m) == 0:
                pairs.append((i, m))
    result = ''
    for pair in pairs:
        result += str(pair[0]) + str(pair[1])
    return result
n = int(input("Введите число n (от 3 до 20): "))
result = generate_password(n)
print(result)