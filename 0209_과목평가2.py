# 1
T = int(input())
for tc in range(1, T+1) :
    N, M = map(int, input().split())
    a = input()  # 문자열은 list를 안해도 인덱스접근이 가능함.
    b = input()

    b_idx = 0
    result = -1

    for a_idx in range(N) :
        if a[a_idx] == b[b_idx] :
            b_idx += 1
            if b_idx >= M :
                break
    if b_idx == M :
        result = a_idx

    print(f'#{tc} {result}')


# 2
T = int(input())
for tc in range(1, T+1) :
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    sums = 0
    maxs = 0

    for r in range(N) :
        for c in range(M) :
            if arr[r][c] == 0 :

                for d in range(4) :
                    nr = r + dr[d]
                    nc = c + dc[d]

                    if 0 <= nr < N and 0 <= nc < M :
                        sums += arr[nr][nc]

                if sums > maxs :
                    maxs = sums
                sums = 0
            
    print(f'#{tc} {maxs}')