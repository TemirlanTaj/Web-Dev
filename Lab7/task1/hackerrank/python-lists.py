if __name__ == '__main__':
    N = int(input())
    arr = []
    prompt = ""
    for i in range(N):
        prompt = input().split(" ")
        if prompt[0] == "append":
            arr.append(int(prompt[1]))
        elif prompt[0] == "insert":
            arr.insert(int(prompt[1]), int(prompt[2]))
        elif prompt[0] == "pop":
            arr.pop()
        elif prompt[0] == "remove":
            arr.remove(prompt[1])
        elif prompt[0] == "sort":
            arr.sort()
        elif prompt[0] == "reverse":
            arr.reverse()
        elif prompt[0] == "print":
            print(arr)