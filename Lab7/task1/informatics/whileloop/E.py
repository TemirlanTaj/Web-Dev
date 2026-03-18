n = int(input())
twoPow = 1
power = 0

while twoPow < n:
    twoPow *= 2
    power += 1

print(power)