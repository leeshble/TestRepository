T = int(input())

for t in range(T):
    inputList = list(map(int, input().split()))
    result = '='
    if inputList[0] > inputList[1]:
        result = '>'
    elif inputList[0] < inputList[1]:
        result = '<'

    print(f"#{t+1} {result}")
