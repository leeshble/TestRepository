T = int(input())

for t in range(T):
    X, Y, N = map(int, input().split())

    result = 0
    while max(X, Y) <= N:
        if X < Y:
            X += Y
        else:
            Y += X
        result += 1

    print(result)