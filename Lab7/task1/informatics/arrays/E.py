size = int(input())

def getsign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

arr = list(map(int, input().split()))
flag = False

for i in range(size - 1):
    if getsign( arr[i] ) == getsign( arr[i+1] ):
        flag = True
        break

if flag:
    print("YES")
else:
    print("NO")
