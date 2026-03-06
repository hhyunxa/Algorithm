# 14510. 나무 높이
T = int(input())

for tc in range(1, T+1):
    # 나무의 개수
    N = int(input())
    heights = list(map(int, input().split()))
    max_height = max(heights)
    ans = 0
    
    one_count = 0
    two_count = 0
    for height in heights():
        if height == heighest_tree:
            continue
        one_count += (heighest_tree - height) % 2    # 0 또는 1
        two_count += (max_height - height) // 2   # 최대한 2 블럭 확보

    while two_count - one_count > 1:
        two_count -= 1
        one_count += 2

    if one_count < two_count:
        ans = 2*one_count -1
    else:
        ans = 2*two_count

    print(f'{tc} {ans}')
