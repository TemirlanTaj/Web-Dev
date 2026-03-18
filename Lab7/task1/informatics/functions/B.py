def power(num, pownum):
    if pownum == 0:
        return 1
    elif pownum < 0:
        return 1 / power(num, -pownum)
    else:
        temp = num
        for i in range(pownum - 1):
            num = num * temp
        return num

arr = list(map(int, input().split()))

print( power(arr[0], arr[1]) )

# print( arr[0] ** arr[1] )