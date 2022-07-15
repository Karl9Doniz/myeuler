# Even Fibonacci numbers

def calculate_sum(n):
    if n <= 0:
        return 0

    f = [0] * (n + 1)
    f[1] = 1

    sum = f[0] + f[1]

    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
        if f[i] % 2 == 0:
            sum = sum + f[i]

    return sum


print(calculate_sum(34) - 1)
