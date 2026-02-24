# 2001. 파리퇴치
T = int(input())
for tc in range(1, T+1) :
    N, M = map(int, input().split())
    arr_N = [list(map(int, input().split())) for _ in range(N)]

    maxs = 0

    for r in range(N-M+1) :
        for c in range(N-M+1) :

            sums = 0
            
            for i in range(r, r+M) :
                for j in range(c, c+M) :
                    sums += arr_N[i][j]

            if sums > maxs :
                maxs = sums

    print(f'#{tc} {maxs}')

# 1954. 달팽이 숫자
# 0우 1하 2좌 3상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1) :
    N = int(input())

    ans = [[0] * N for _ in range(N)]

    count=1
    r, c = 0, 0
    d = 0

    for _ in range(N*N) :
        ans[r][c] = count

        count += 1

        if count > N*N :
            break
        
        if c+dc[d] > N-1 or r+dr[d] > N-1 or c+dc[d] < 0 or r+dr[d] < 0 or ans[r+dr[d]][c+dc[d]] != 0 :
            d += 1
            d %= 4

        r = r + dr[d]
        c = c + dc[d]

    print(f'#{tc}')
    for row in ans:
        print(*row)

    