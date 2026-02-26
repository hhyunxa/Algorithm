# 백준 15686. 치킨 배달
def dfs(count, idx):   # chickens중에 M개 고르기
    if count == M:     # M개를 골랐으면
        distance = 0
        for home in homes:           # return min_distance 
            distance += chicken_distance(home, picked_chickens)   # 치킨거리들의 합으로 도시의치킨거리 구하기
        result.append(distance)   # result에 도시의치킨거리 저장
    else:
        for i in range(idx, len(chickens)):
            picked_chickens.append(chickens[i])   # pick_chickens에 chickens의 값 골라 넣기
            dfs(count+1, i+1)    # count가 M이 될때까지 재귀함수
            picked_chickens.pop()    # ex) a,b -> a,c

def chicken_distance(home, picked_chickens):   # 치킨거리 구하기(하나의 home골라서)
    min_distance = 9999999
    for chicken in picked_chickens:   # picked_chickens에서 chicken하나 고르기
        dis = abs(home[0] - chicken[0]) + abs(home[1] - chicken[1])   # 하나의home이랑 하나의chicken사이의 치킨거리 구하기
        if dis < min_distance:
            min_distance = dis
    return min_distance    # pick_chickens중에서 home과의 치킨거리가 가장 짧은 애를 리턴

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

chickens = []
homes = []
picked_chickens = []
result = []

for r in range(N):
        for c in range(N):
                if arr[r][c] == 1:
                    homes.append((r, c))
                elif arr[r][c] == 2:
                    chickens.append((r, c))

dfs(0, 0)
print(min(result))


# 1219. [S/W 문제해결 기본] 4일차 - 길찾기
def DFS(start):
    global result
    for next_node in adj_list[start]:
        if next_node == 99:
            result = 1   # DFS 는 return 1이 안됨. 그 작은 DFS에서만 1을 반환함. 우린 전체에서 해야함.
        else:
            DFS(next_node)
                
for _ in range(1, 11):
    t, N = map(int,input().split())   
    arr = list(map(int, input().split()))

    adj_list = [[] for _ in range(100)]

    for i in range(0,len(arr),2):
        adj_list[arr[i]].append(arr[i+1])

    result = 0
    DFS(0)
    print(f'#{t} {result}')


# 4871. [파이썬 S/W 문제해결 기본] 4일차 - 그래프 경로
def dfs(S):
    global result
    for next_node in adj_list[S]:
        if next_node == G:
            result = 1
        else:
            dfs(next_node)
        
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        adj_list[a].append(b)
    S, G = map(int, input().split())

    result = 0
    dfs(S)
    print(f'#{tc} {result}')