def minimal(a, b, c, d):
    if a < b:
        if a < c:
            if a < d:
                return a
            else:
                return d
        else:
            if c < d:
                return c
            else:
                return d
    else:
        if b < c:
            if b < d:
                return b
            else:
                if d < c:
                    return d
                else:
                    return c
        else:
            if c < d:
                return c
            else:
                return d


arr = list(map(int, input().split()))

print(minimal(arr[0], arr[1], arr[2], arr[3]))
