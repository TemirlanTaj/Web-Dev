size = int(input())

arr = list(map(int, input().split()))

index = 0
while index < size:
    print(arr[index], end=" ")
    index += 2