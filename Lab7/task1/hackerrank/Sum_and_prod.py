import numpy

size = input().split(" ")
arr = []

for i in range(int(size[0])):
    arr.append(list(map(int, input().split())))

summ = numpy.sum(arr, axis=0)
print(numpy.prod(summ))