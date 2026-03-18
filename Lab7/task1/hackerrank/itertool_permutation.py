# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

input = list(map(str, input().split()))

res = list(itertools.permutations(input[0], int(input[1])))

for i in res:
    print("".join(i))