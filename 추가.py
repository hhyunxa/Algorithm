arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# 행 번호(r)부터 잡자
for r in range(len(arr)) :
    # 열 번호(c) 잡자
    for c in range(len(arr[r])) :
        print(arr[r][c], end=' ')
    print()

# 열 번호(c)부터 잡자
for c in range(3) :
    # 행 번호(r) 잡자
    for r in range(3) :
        print(arr[r][c], end=' ')
    print()

print(list(zip(*arr)))  # 추천방법은 아님. 튜플로 뽑힘. map, list로 해결.

# 방향 입력을 무한으로 받고, 이동, 안되면 안된다고 출력, 이동하면 ㅇㅣ동한 위치 출력
# 상 0, 하 1, 좌 2, 우 3
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N = 5  # 행의길이
M = 5  # 열의길이
r, c = 2, 2  # 초기위치

while True :
    dir = int(input())

    if 0 <= r+dr[dir] < N and 0 <= c+dc[dir] < M :
        r = r+dr[dir]
        c = c+dc[dir]
        print('이동한 좌표 :', r, c)
    else :
        print('이동 불가능합니다.')

        break

# 코드트리
n = int(input())

def rectangle(n) :
    arr = [[0] * n for _ in range(n)]
    num = 1

    for r in range(n) :
        for c in range(n) :
            arr[r][c] = num
            num += 1

            if num == 10 :
                num = 1

            print(arr[r][c], end = ' ')
        print()

rectangle(n)

# 버블정렬
def bubble_sort(a, N) :
    for i in range(N-1, 0, -1) :
        for j in range(i) :
            if a[j] > a[j+1] :
                a[j], a[j+1] = a[j+1], a[j]

# 선택정렬
def selection_sort(a, N) :
    for i in range(N-1) :
        min_dix = i
        for j in range(i+1, N) :
            if a[min_dix] > a[j] :
                min_dix = j
        a[i], a[min_dix] = a[min_dix], a[i]
    

# 순열/조합 구현
numbers = [1,2,3,4,5]

# 원복 필요
pick_numbers1 = []
# 원복 불필요
pick_numbers2 = [0]*3

picks = []

# 중복 순열
def perm(count):
    if count == 3:
        print(pick_numbers1)
        return
    
    # 1. 숫자를 1~N 중에 하나를 골라서 뽑는다
    #    내가 고를 숫자의 인덱스는 i
    for i in range(len(numbers)):
        pick_numbers1.append(numbers[i])
        # 2. 다음 재귀 호출
        perm(count+1)
        pick_numbers1.pop()
        
# idx : 탐색 범위의 첫 인덱스
def comb(count, idx):
    if count == 3:
        print(pick_numbers1)
        return
    
    for i in range(idx, len(numbers)):
        pick_numbers1.append(numbers[i])
        # 조합
        comb(count+1, i+1)
        # 중복 조합
        # comb(count+1, i)
        pick_numbers1.pop()
        
# 순열
def perm2(count):
    if count == 3:
        picks.append(pick_numbers2[:])
        return
    
    for i in range(len(numbers)):
        if visited[i]:
            continue
        visited[i] = 1
        pick_numbers2[count] = numbers[i]
        perm2(count+1)
        visited[i] = 0    
        
# perm(0)
# comb(0, 0)
visited = [0]*len(numbers)
perm2(0)
print(picks)
    





