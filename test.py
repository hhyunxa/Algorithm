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