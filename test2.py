dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    M, A = map(int, input().split())
    path_A = list(map(int, input().split()))
    path_B = list(map(int, input().split()))
    bc_list = []
    for _ in range(A):
        x, y, C, P = map(int, input().split())
        bc_list.append((x, y, C, P))

    