x = input()
res = []

for i in range(len(x) - 1, -1, -1):
    res.append(x[i])
print(int("".join(res)))

# print(x[::-1])