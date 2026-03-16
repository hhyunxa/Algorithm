# 1486. 장훈이의 높은 선반
def dfs(idx, sum_h):
    global ans
    if idx == N:
        if sum_h >= B:
            if ans > sum_h:
                ans = sum_h
        return
    
    dfs(idx + 1, sum_h + H[idx])   # 이번 점원 포함

    dfs(idx + 1, sum_h)   # 이번 점원 미포함

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))

    ans = 99999999
    dfs(0, 0)
    print(f'#{tc} {ans - B}')