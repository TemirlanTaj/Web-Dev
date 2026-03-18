number = int(input())
res = []

for i in range(1, number + 1):
    if number % i == 0:
        res.append(i)
for i in res:
    print(i, end=" ")