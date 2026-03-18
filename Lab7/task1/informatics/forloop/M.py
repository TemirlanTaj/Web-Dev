n = int(input())
temp = 0
zeroCounter = 0

for i in range(n):
    temp = int(input())
    if temp == 0:
        zeroCounter += 1

print(zeroCounter)