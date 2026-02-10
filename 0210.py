# 4871. [파이썬 S/W 문제해결 기본] 4일차 - 그래프 경로
T = int(input())
for tc in range(1, T+1) :
    V, E = map(int, input().split())

    # 인접리스트 만들기
    adj_list = [[] for _ in range(V+1)]

    for _ in range(E) :
        a, b = map(int, input().split())
        adj_list[a].append(b)

    S, G = map(int, input().split())

    # DFS 시작
    visited = [0] * (V+1)
    stack = []

    curr = S
    visited[curr] = 1
    answer = 0

    while True :
        if curr == G :  # 도착하면 1, break
            answer = 1
            break
    
        for i in adj_list[curr] :  # 현재노드에서 갈 수 있는 다음노드들 탐색
            if visited[i] == 0 :   # 다음노드를 방문했는데 0이면,즉 아직 방문 안했던 노드면
                stack.append(curr) # 다음노드 이동 전에 현재노드를 스택에 저장
                curr = i           # 다음노드로 이동
                visited[curr] = 1  # 다음노드 visited를 1로 저장. 즉 방문했다고 기록하기
                break
        else :
            if stack :
                curr = stack.pop()
            else :
                break

    print(f'#{tc} {answer}')


# 1219. [S/W 문제해결 기본] 4일차 - 길찾기
T = 10
for tc in range(1, T+1) :
    _, E = map(int, input().split())

    # 인접리스트 만들기
    adj_list = [[] for _ in range(100)]

    info = list(map(int, input().split()))  # list를 해줘야함. 
    for i in range(0, E*2, 2) :
        a, b = info[i], info[i+1]           # a와 b를 인덱스로 꺼내기 때문에
        adj_list[a].append(b)

    # DFS 시작
    stack = []
    visited = [0] * 100
    curr = 0
    visited[curr] = 1
    answer = 0

    while True :
        if curr == 99 :
            answer = 1
            break

        for w in adj_list[curr] :
            if visited[w] == 0 :
                stack.append(curr)
                curr = w
                visited[curr] = 1
                break
        else :
            if stack :
                curr = stack.pop()
            else :
                break

    print(f'#{tc} {answer}')


# 백준. DFS와 BFS
N, M, V = map(int, input().split())

adj_list = [[] for _ in range(N+1)]

for _ in range(M) :
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

for i in range(1, N+1) :
    adj_list[i].sort()    # 정점번호가 작은것부터 방문

visited = [0] * (N+1)
stack = []
curr = V
visited[curr] = 1
path = [curr]   # 경로를 저장해줌

while True :
    for w in adj_list[curr] :
        if visited[w] == 0 :
            stack.append(curr)
            curr = w
            visited[curr] = 1
            path.append(curr)   # 경로를 저장
            break
    else :
        if stack :
            curr = stack.pop()
        else :
            break

print(*path)   # 경로 출력