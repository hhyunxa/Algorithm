# 1231. [S/W 문제해결 기본] 9일차 - 중위순회
def inorder(node):
    # 왼쪽 자식노드가 있을 때만
    if node*2 <= N:
        inorder(node*2)
    print(tree[node], end='')
    # 오른쪽 자식노드가 있을 때만
    if node*2+1 <= N:
        inorder(node*2+1)
    # print(tree[node], end='')  후위순위

T = 10
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    for idx in range(1, N+1):
        info = input().split()
        tree[idx] = info[1]

    print(f'#{tc} ', end='')

    inorder(1)
    print()