size = int(input())

arr = list(map(int, input().split()))

counter = 0
for i in range(1, size - 1):
    if arr[i-1] < arr[i] and arr[i+1] < arr[i]:
        counter += 1

print(counter)