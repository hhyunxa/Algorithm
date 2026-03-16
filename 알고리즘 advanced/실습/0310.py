# 2117. [모의 SW 역량테스트] 홈 방범 서비스
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_homes = 0
    homes = []
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 1:
                homes.append((r, c))

    for r in range(N):
        for c in range(N):
            for K in range(1, 2*N):
                current_home = 0

                for hr, hc in homes:
                    distance = abs(r-hr) + abs(c-hc)   # 마름모는 dr, dc 이용하지 말고, 멘헤튼 거리 이용.
                    if distance <= K-1:   # 멘헤튼 거리가 범위(K-1)안에 들어오면 마름모 안에 있는거임.
                        current_home += 1               # K = 2 > 중심으로 부터 1칸 떨어짐 > K-1

                profit = (current_home*M) - (K*K + (K-1)*(K-1))

                if profit >= 0:
                    if max_homes < current_home:
                        max_homes = current_home

    print(f'#{tc} {max_homes}')