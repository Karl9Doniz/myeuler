# Multiples of 3 or 5

n = int(input())
sum = 0

for i in range(1, n):
    if (i % 3 == 0) or (i % 5 == 0):
        sum += i


print(sum)
