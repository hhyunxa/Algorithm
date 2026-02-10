# 1
T = int(input())
for tc in range(1, T+1) :
    N_len, M_len = map(int, input().split())
    N = input()  # 문자열은 list를 안해도 인덱스접근이 가능함.
    M = input()

    M_idx = 0
    result = -1

    for N_idx in range(N_len) :
        if N[N_idx] == M[M_idx] :
            M_idx += 1
            if M_idx >= M_len :
                break
    if M_idx == M_len :  
        result = N_idx  

    print(f'#{tc} {result}')


# 2
T = int(input())
for tc in range(1, T+1) :
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    maxs = 0

    for r in range(N) :
        for c in range(M) :
            if arr[r][c] == 0 :
                count = 0
                for i in range(4) :
                    nr = r+dr[i]
                    nc = c+dc[i]

                    if 0 <= nr < N and 0 <= nc < M :
                        count += arr[nr][nc]

                if count > maxs :
                    maxs = count
                
    print(f'#{tc} {maxs}')
