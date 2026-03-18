x = input()
d = input()
counter = 0

for i in range(0, len(x)):
    if x[i] == d:
        counter += 1

print(counter)