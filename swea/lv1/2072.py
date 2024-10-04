T = int(input())

for t in range(T):
    inputList = list(map(int, input().split()))
    result = 0
    for i in range(len(inputList)):
        if inputList[i] % 2 != 0:
            result += inputList[i]

    print(f"#{t+1} {result}")
