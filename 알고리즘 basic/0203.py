# 1208. [S/W 문제해결 기본] 1일차 - Flatten
for tc in range(1, 11) :
    dump_count = int(input())
    box_len = list(map(int, input().split()))

    for _ in range(dump_count) :
        max_idx = box_len.index(max(box_len))
        min_idx = box_len.index(min(box_len))

        box_len[max_idx] -= 1
        box_len[min_idx] += 1

    result = max(box_len) - min(box_len)

    print(f'#{tc} {result}')

# 26045. 부분수열판별
t = int(input())
for tc in range(1, t+1) :
    n, m = map(int, input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    b_idx = 0
    result = 'No'

    for i in a :
        if i == b[b_idx] :
            b_idx += 1
            if b_idx >= m :
                break

    if b_idx == m :
        result = 'Yes'
            
    print(f'#{tc} {result}')

# 4834. [파이썬 S/W 문제해결 기본] 1일차 - 숫자 카드
t = int(input())
for tc in range(1, t+1) :
    n = int(input())
    a = list(map(int, input()))

    counts = [0] * 10

    for i in a :
        counts[i] += 1

    numbers = -1
    numbers_counts = -1

    for j in range(9, -1, -1) :
        if counts[j] > numbers_counts :
            numbers_counts = counts[j]
            numbers = j

    print(f'#{tc} {numbers} {numbers_counts}')

# 4831. [파이썬 S/W 문제해결 기본] 1일차 - 전기버스
t = int(input())
for tc in range(1, t+1) :
    k, n, m = map(int, input().split())
    m_number = list(map(int, input().split()))

    bus_stop = [0] * (n+1)

    for i in m_number :
        bus_stop[i] = 1

    current = 0
    count = 0

    while current + k < n :
        for step in range(k, 0, -1) :
            if bus_stop[current + step] :
                current += step
                count += 1
                break
        else :
            count = 0
            break

    print(f'#{tc} {count}')


