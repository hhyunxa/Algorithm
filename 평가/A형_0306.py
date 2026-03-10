# swea 1767. [SW Test 샘플문제] 프로세서 연결하기
def dfs(core_cnt, wire_cnt, idx):
    global max_cores, min_wires

    if idx == len(cores):
        if core_cnt > max_cores:   # 연결된 코어가 더 많으면 갱신
            max_cores = core_cnt
            min_wires = wire_cnt
        elif core_cnt == max_cores:   # 코어 수가 같으면
            if wire_cnt < min_wires:  
                min_wires = wire_cnt   # 전선 합이 더 작은거 선택
        return
    
    r, c = cores[idx]   # core 하나 선택함

    for d in range(4):   # 4방향 탐색
        nr = r + dr[d]
        nc = c + dc[d]

        tmp_wire_cnt = 0   # 선택한 core하나의 와이어 길 세기
        possible = False

        while 0<=nr<N and 0<=nc<N:
            if arr[nr][nc] == 1 or visited[nr][nc] == 1:
                break
            nr += dr[d]
            nc += dc[d]
            tmp_wire_cnt += 1   # 와이어 길 하나 증가
        else:   # break 없이 끝까지 왔다면, 즉, 와이어 길을 끝까지 다 가면
            possible = True   # 연결 가능
        
        if possible:
            tr, tc = r, c
            for _ in range(tmp_wire_cnt):   # 온 와이어 길 만큼
                tr += dr[d]
                tc += dc[d]
                visited[tr][tc] = 1   # 방문 표시. 즉, 전선 깔기

            dfs(core_cnt+1, wire_cnt+tmp_wire_cnt, idx+1)   # 전선 깐 상태에서 다음 코어 이동

            tr, tc = r, c
            for _ in range(tmp_wire_cnt):
                tr += dr[d]
                tc += dc[d]
                visited[tr][tc] = 0   # 방문 지우기. 즉, 전선 지우기

    dfs(core_cnt, wire_cnt, idx+1)   # 현재 코어 연결 안하고 다음 코어로 넘어감

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0] * N for _ in range(N)]
    cores = []

    for i in range(1, N-1):
        for j in range(1, N-1):
            if arr[i][j] == 1:
                cores.append((i, j))

    max_cores = 0
    min_wires = 999999999999

    dfs(0, 0, 0)
    print(f'${tc} {min_wires}')


# 백준 17472. 다리 만들기 2