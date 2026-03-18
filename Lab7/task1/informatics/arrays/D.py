size = int(input())

arr = list(map(int, input().split()))
counter = 0

for i in range(size - 1):
    if arr[i] < arr[i+1]:
        counter += 1

print(counter)