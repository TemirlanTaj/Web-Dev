number = int(input())
res = 0

for i in range(1, int(number**0.5) + 1):
    if number % i == 0:
        if i*i == number:
            res += 1
        else:
            res += 2
print(res)