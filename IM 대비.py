# 23569. 두개의 탑
T = int(input())
for tc in range(1, T+1) :
    A, N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    new_numbers = sorted(numbers, reverse=True)
    new_numbers_idx = 0
    hN, hM = 1, 1
    count = 0

    while hN <= N and hM <= M :
        count += new_numbers[new_numbers_idx] * hN
        new_numbers_idx += 1
        count += new_numbers[new_numbers_idx] * hM
        new_numbers_idx += 1
        hN += 1
        hM += 1

    while hN <= N :
        count += new_numbers[new_numbers_idx] * hN
        new_numbers_idx += 1
        hN += 1

    while hM <= M :
        count += new_numbers[new_numbers_idx] * hM
        new_numbers_idx += 1
        hM += 1

    print(f'#{tc} {count}')


# 1979. 어디에 단어가 들어갈 수 있을까
T = int(input())
for tc in range(1, T+1) :
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    count = 0
    result = 0

    for r in range(N) :
        for c in range(N) :
            if puzzle[r][c] == 1 :  # 1의 갯수를 세기
                count += 1
            else :
                if count == K :     # 0을 만났을 때 1의 갯수가 K면 result를 +1 하기
                    result += 1
                count = 0           # 0을 만났으니까 1을 다시 처읍부터 count 헤야함. 즉, count 초기화
        if count == K :             # for 문을 다 돌았을 때도 count(1의 총 갯수)가 K가 되었으면 
            result += 1             # result를 +1 하기
        count = 0
                
            
    for c in range(N) :
        for r in range(N) :
            if puzzle[r][c] == 1 :
                count += 1
            else :
                if count == K :
                    result += 1
                count = 0
        if count == K :
            result += 1
        count = 0

    print(f'#{tc} {result}')


# 23795. 우주 괴물
T = int(input())
for tc in range(1, T+1) :
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for r in range(N) :
        for c in range(N) :
            if arr[r][c] == 2 :

                for d in range(4) :
                    nr = r + dr[d]
                    nc = c + dc[d]

                    while 0 <= nr < N and 0 <= nc < N :
                        if arr[nr][nc] == 1 :
                            break
                        if arr[nr][nc] == 0 :
                            arr[nr][nc] = 1
                        nr = nr + dr[d]
                        nc = nc + dc[d]
                            
    count = 0
    for r in range(N) :
        for c in range(N) :
            if arr[r][c] == 0 :
                count += 1

    print(f'#{tc} {count}')


# 야구팀 짜기
'''
input
3
4 2
6 4 2 3
4 3
1 2 3 4
4 1
1 3 7 5

output
#1 3
#2 4
#3 1
'''


# 공 굴리기
'''
input
3
5
19 57 74 73 94
26 27 32 98 61
40 88 49 38 25
21 66 53 95 46
80 23 58 39 89
7
40 49 56 83 84 31 11
42 95 12 16 21 19 26
98 93 29 68 10 92 82
23 13 24 58 35 25 47
17 66 39 67 70 14 87
22 34 46 94 69 96 89
62 88 50 51 61 71 86
9
90 57 65 18 25 93 64 11 54
95 19 80 37 63 44 15 14 10
89 59 46 70 38 36 21 51 97
53 47 60 88 40 48 79 56 55
83 13 27 86 45 71 75 28 84
30 20 29 35 99 98 61 94 23
85 42 43 22 16 77 31 78 34
74 26 73 92 50 72 87 49 32
68 24 91 12 17 82 69 67 81

output
6
10
9
'''