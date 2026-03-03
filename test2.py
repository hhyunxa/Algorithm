T= int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2:

                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]

                    while 0<=nr<N and 0<=nc<N:
                        if arr[nr][nc] == 1:
                            break
                        if arr[nr][nc] == 0:
                            arr[nr][nc] = 3
                        nr += dr[d]
                        nc += dc[d]

    count = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                count += 1
        
    print(f'#{tc} {count}')