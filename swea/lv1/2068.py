T = int(input())

for t in range(T):
    inputList = list(map(int, input().split()))
    result = max(inputList)

    print(f"#{t+1} {result}")
