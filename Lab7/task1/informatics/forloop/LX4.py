from math import pow
binaryNum = input() # 1001
intRes = 0          # 0123

for i in range(0, len(binaryNum)):
    intRes += pow( 2, int(len(binaryNum)-1-i) ) * int(binaryNum[i])
    # print(intRes)
print(int(intRes))