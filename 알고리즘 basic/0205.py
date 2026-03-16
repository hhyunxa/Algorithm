# 1210. [S/W 문제해결 기본] 2일차 - Ladder1
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for _ in range(10) :
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    for c in range(100) :
        if ladder[99][c] == 2 :
            r, c = 99, c
            break

    while r > 0 :

        # 이거 너무 중요!! 왔던길 안돌아올라면(좌우이동시) 지나간길은 0으로 바꿔주기
        ladder[r][c] = 0
        d = 0

        # 왼쪽이 1인지 확인
        if 0 <= c+dc[2] < 100 and ladder[r+dr[2]][c+dc[2]] == 1 :
            d = 2

        # 오른쪽이 1인지 확인
        elif 0 <= c+dc[3] < 100 and ladder[r+dr[3]][c+dc[3]] == 1 :
            d = 3

        r = r + dr[d]
        c = c + dc[d]

    print(f'#{tc} {c}')


# 1966. 숫자를 정렬하자
def bubble_sort(a, N) :
    for i in range(N-1, 0, -1) :
        for j in range(i) :
            if a[j] > a[j+1] :
                a[j], a[j+1] = a[j+1], a[j]

T = int(input())
for tc in range(1, T+1) :
    N = int(input())
    numbers = list(map(int, input().split()))

    bubble_sort(numbers, N)

    print(f'#{tc}', *numbers)


# 4836. [파이썬 S/W 문제해결 기본] 2일차 - 색칠하기
T = int(input())
for tc in range(1, T+1) :
    N = int(input())

    arr = [[0] * 10 for _ in range(10)]

    for _ in range(N) :
        r1, c1, r2, c2, colors = list(map(int, input().split()))

        for r in range(r1, r2+1) :
            for c in range(c1, c2+1) :
                arr[r][c] += colors

    count = 0

    for i in range(10) :
        for j in range(10) :
            if arr[i][j] == 3 :
                count += 1

    print(f'#{tc} {count}')


# 4839. [파이썬 S/W 문제해결 기본] 2일차 - 이진탐색
def func(total_P, P) :

    count = 0
    l = 1

    while True :
        ans = (l + total_P) // 2
        count += 1

        if ans < P :
            l = ans
        elif ans > P :
            total_P = ans
        else :
            return count
        
T = int(input())
for tc in range(1, T+1) :
    total_P, P_A, P_B = list(map(int, input().split()))
    
    count_A = func(total_P, P_A)
    count_B = func(total_P, P_B)

    if count_A > count_B :
        print(f'#{tc} B')
    elif count_A < count_B :
        print(f'#{tc} A')
    else :
        print(f'#{tc} 0')




