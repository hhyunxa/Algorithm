T = int(input())
for tc in range(1, T+1) :
    N = int(input())

    arr = [[0] * N for _ in range(N)]

    for r in range(N) :
        for c in range(N) :