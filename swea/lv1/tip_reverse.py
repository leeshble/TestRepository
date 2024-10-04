
inputList = list(map(int, input().split()))
inputList.reverse()

result = ' '.join(str(s) for s in inputList)
print(f"#{t+1} {result}")
