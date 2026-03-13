# 20551. 증가하는 사탕 수열
'''
증가하는 사탕 수열
사탕을 담은 상자 (A, B, C)
- 순증가
    - A, B 상자의 사탕을 먹어서 만들자
    - B 상자를 먼저 해결하고, A 상자를 보자
        - B 상자: C 상자보다 작게
        - A 상자: B 상자보다 작게
- 각 상자는 1개 이상의 사탕이 남아야 한다.
    - C는 3 이상 / B는 2 이상

1. 완전탐색
1 <= A, B, C <= 3000
- B를 C보다 작을 때까지 하나씩 먹자(빼자)
- A를 B보다 작을 떄까지 하나씩 먹자(빼자)
- 최악의 경우 (3000, 3000, 3)
    - 2999 + 2998
    - [참고] A상자와 B상자를 N개 씩 먹는 모든 경우의 수를 다 본다 (3000 * 3000 --> 충분히 괜찮다)
        - 시간초과 발생한다.

2. 규칙을 세우자
- B = C - 1 / A = B - 1로 만들면 된다.
'''

T = int(input())
for tc in range(1, T+1):
    A, B, C = map(int, input().split())

    # 1. 문제 조건이 불가능한 케이스
    if B<2 or C<3:
        print(f'#{tc} -1')
        continue

    # 2. B = C - 1 / A = B - 1로 만들면 된다.
    eat_count = 0

    # B 상자
    if B >= C:
        eat_count += B - (C - 1)   # 높이의 차이 +1 만큼 먹는다
        B = C - 1

    # A 상자
    if A >= B:
        eat_count += A - (B - 1)
        A = B - 1

    print(f'#{tc} {eat_count}')


# 10580. 전봇대
'''
전선 N개
- 교차점 발생
- 교차점의 개수를 count

교차점의 발생 규칙
새로운 선이
    1. 기존의 선보다 시작점은 높고, 도착점은 낮다.
    2. 기존의 선보다 시작점은 낮고, 도착점은 높다.
새로운 선이 들어오면, 기존의 모든 선들과 비교
-> 완전 탐색
    - 시간복잡도 - O(N^2), 연산횟수 - 1 + 2 + 3 + ... + N - 1(약 50만번)
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    wires = []   # 기존선들을 저장할 리스트
    answer = 0   # 교차점 수

    for _ in range(N):
        start, end = map(int, input().split())

        # 기존의 모든 선들과 시작점, 도착점을 비교
        for prev_start, prev_end in wires:
            # 1. 기존의 선보다 시작점은 높고, 도착점은 낮다.
            if start > prev_start and end < prev_end:
                answer += 1
            # 2. 기존의 선보다 시작점은 낮고, 도착점은 높다.
            if start < prev_start and end > prev_end:
                answer += 1
            
        # 기존 목록에 start, end 를 추가
        wires.append((start, end))

    print(f'#{tc} {answer}')


# 1953. 탈주범 검거
'''
지하터널
- 터널들을 이동 (상하좌우)
    - 델타 배열 써야하는구나
- 이동 못하는 경우들도 존재
    - 현재 내 위치에서 뚫려 있는 곳만 이동 가능
    - 다음 위치의 입구가 뚫려있는 곳으로만 이동 가능
- 시간 (L)
    - 시간 내로 이동 가능한 위치의 개수

맨홀 뚜겅(y, x)으로 부터 시간 내로 갈 수 있는 모든 위치의 수
- 특정 좌표로부터 점점 넓혀나가는 그림
    --> BFS로 접근하자 !

- BFS의 복잡도
    - queue에 얼마나 많은 데이터가 들어가는가 ?
    - O(V + E)
        - V: 정점의 수 / E: 간선의 수
        - 정점의 수 = 최대 2,500개
        - 간선의 수 = 2500 * 4(상하좌우) = 10, 000개
        -> 12,500 ==> 여유롭다.

BFS 상세
    - 탐색: 상하좌우
    - 이동이 불가능한 케이스
        - [델타 배열 기본] 밤위 밖으로 나가면 못감
        - [방문 기록 기본] 이미 방문한 곳은 못감
        - [0이면 못감]
        - [문제조건]
            - 현재 내 위치에서 뚫려 있는 곳만 이동 가능
            - 다음 위치의 입구가 뚫려있는 곳으로만 이동 가능
                -> 델타배열과 동일한 순서로 "이동 가능 여부"를 기록하면 좋음
'''
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 터널들의 종류에 따라서, 이동 가능 여부
types = {
    # 상하좌우 순서
    1: [1, 1, 1, 1],
    2: [1, 1, 0, 0],
    3: [0, 0, 1, 1],
    4: [1, 0, 0, 1],
    5: [0, 1, 0, 1],
    6: [0, 1, 1, 0],
    7: [1, 0, 1, 0]
}

def bfs(R, C):
    q = deque([(R, C)])
    visited[R][C] = 1

    while q:
        now_y, now_x = q.popleft()
        dirs = types[graph[now_y][now_x]]

        # 현재 좌표로부터 갈 수 있는 모든 노드를 확인
        # - 우리 문제에서는 상하좌우
        # - 이동 가능한 다음 좌표만 q에 추가
        for i in range(4):
            # i 방향이 안뚫리면 못감
            if dirs[dir] == 0:
                continue

            ny = now_y + dy[dir]
            nx = now_x + dx[dir]

            # [델타 배열 기본] 밤위 밖으로 나가면 못감
            if ny<0 or ny>=N or nx<0 or nx>=M:
                continue
            # [방문 기록 기본] 이미 방문한 곳은 못감
            if visited[ny][nx]:
                continue
            # [0이면 못감]
            if graph[ny][nx] == 0:
                continue
            
            # 다음 위치의 입구가 뚫려있는 곳으로만 이동 가능
            next_dirs = types[graph[ny][nx]]

            # 현재 상좌 -> next_dirs가 하우가 안뚫리면 못감
            if dir % 2 == 0 and next_dirs[dir + 1] == 0:
                continue
            # 현재 하우 -> next_dirs가 상좌가 안뚫리면 못감
            if dir % 2 == 1 and next_dirs[dir - 1] == 0:
                continue
            # L 시간을 넘어가면 안봐도 된다
            if visited[ny][nx] + 1 > L:
                continue

            # 시간을 +1 누적하면서 이동
            visited[ny][nx] = visited[now_y][now_x] + 1
            q.append((ny, nx))
            

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    bfs(R, C)

    cnt = 0
    # L 시간 내로 방문한 곳을 count
    for i in range(N):
        for j in range(M):
            if 0 < visited[i][j] <= L:
                cnt += 1

    print(f'#{tc} {cnt}')


# 5656. 벽돌깨기
'''
N번 쏘기
- 연쇄 작용
    - 벽돌 숫자에 맞게 상하좌우로 폭발
- 연쇄 작용 이후
    - 벽돌이 밑으로 떨어진다

- 최대한 많은 벽돌을 제거
    - 모든 좌표에 구슬을 떨어뜨려 보아야 계산 가능
    -> 완전 탐색 문제
    - N번 쏜다 == depth 4
    - 1번당 구슬의 위치는 12종류 == branch: 12

- 가지치기 가능한 조건이 있니?
    - 남은 벽돌이 0개라면 종료
    -> 남은 벽돌도 변수로 관리하자

1. 최소 벽돌
- 현재 벽돌이 다 꺠지면 더 이상 할 필요 없다. ( 현재 벽돌 수를 관리)
2. N번의 구슬을 쏘자
- 모든 케이스를 보아야 한다(0000 ~ 11 11 11 11)
- 한번 쏘았을 때
    - 연쇄 작용 (bfs)
        - 델타 배열
    - 빈칸 매우기
- 연쇄 작용하면 원본 배열이 수정될 수 있다.
    1. 원본 배열을 저장해두고, 수정 후 원상복구하자
    2. 원본 배열을 복사해서 복사된 배열을 수정하고 다음 재귀로 전달하자
'''
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# depth: 4
# branch: 12 (0~11 번째 열에 쏜다)
def recur(cnt, remain_blocks, now_arr):
    global min_answer

    if cnt == N or remain_blocks == 0:
        min_answer = min(min_answer, remain_blocks)
        return

    # 모든 열에 구슬을 쏴본다
    for col in range(W):
        # 연쇄 작용
        # - col 에 구슬을 쏘기 전 상태를 복사
        #   - [주의] 얕은 복사 주의! 깊은 복사로 해주어야 한다.
        # - 복사된 리스트의 col 자리에 구슬을 떨군다
        copy_arr = [row[:] for row in now_arr]

        # 폭발이 시작되는 row 를 찾아야한다
        row = -1
        for r in range(H):
            if copy_arr[r][col]:
                row = r
                break

        # 벽돌이 없는 열은 검사하지 않는다.
        if row == -1:
            continue

        # 해당 row, col 의 숫자부터 시작해서 bfs
        # - 좌표 + 해당 벽돌의 숫자
        q = deque([(row, col, copy_arr[row][col])])
        now_remains = remain_blocks - 1  # 남아있는 벽돌 수
        copy_arr[row][col] = 0  # 구슬이 처음 만나는 벽돌 깨고 시작

        # 주변 벽돌을 파괴
        while q:
            r, c, p = q.popleft()

            for k in range(1, p):
                for i in range(4):
                    nr = r + (dy[i] * k)
                    nc = c + (dx[i] * k)

                    # 범위 밖이면 통과
                    if nr < 0 or nr >= H or nc < 0 or nc >= W:
                        continue

                    # 벽돌이 없으면 통과
                    if copy_arr[nr][nc] == 0:
                        continue

                    q.append((nr, nc, copy_arr[nr][nc]))
                    copy_arr[nr][nc] = 0
                    now_remains -= 1

        # 빈칸 메우기
        for c in range(W):
            idx = H - 1
            for r in range(H - 1, -1, -1):
                if copy_arr[r][c]:  # 벽돌이 있다면
                    copy_arr[r][c], copy_arr[idx][c] = copy_arr[idx][c], copy_arr[r][c]
                    idx -= 1

        # 다음 구슬로 이동
        recur(cnt + 1, now_remains, copy_arr)


T = int(input())

for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    min_answer = 1e9  # 최소 벽돌 수 (정답)

    # 현재 블록 수 계산
    blocks = 0  # 현재 블록 수
    for i in range(H):
        for j in range(W):
            if arr[i][j]:
                blocks += 1

    recur(0, blocks, arr)
    print(f'#{tc} {min_answer}')


# 백준 2565. 전깃줄
  