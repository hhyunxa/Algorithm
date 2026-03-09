# 수업
'''
numbers = [1, 2, 3, 4, 5]
N = numbers 길이
M = 뽑을 개수

pick_numbers > 뽑은 숫자 보관

N개 M개를 뽑아 줄 세우는 순열

순열 > 순서가 중요. ex) (1, 2) != (2, 1)
'''
numbers = [1, 2, 3, 4, 5]
N = int(input())
M = 3

pick_numbers = []

def perm(count):
    if count == M:
        print(*pick_numbers)
        return
                                               # continue 안쓰고 하는 법
    for i in range(N):                         # for i in range(N):
        if visited[i] == 1:                    #     if visited[i] == 0:
            continue                           
        visited[i] = 1                         #     visited[i] = 1  
        pick_numbers.append(numbers[i])        #     pick_numbers.append(numbers[i]) 

        perm(count+1)                          #     perm(count+1)  
        
        visited[i] = 0                         #     visited[i] = 0
        pick_numbers.pop()                     #     pick_numbers.pop()

visited = [0]*N
perm(0)

'''
조합 > 구성이 중요. ex) (1, 2) == (2, 1)
'''
numbers = [1, 2, 3, 4, 5]
N = len(numbers)
M = 3

pick_numbers = []

def comb(count, start):
    # 1. 종료 조건: M개를 다 뽑았을 때
    if count == M:
        print(*pick_numbers)
        return
    
    # 2. 반복문: 'start' 인덱스부터 시작해서 중복 선택 방지
    for i in range(start, N):
        pick_numbers.append(numbers[i]) # 숫자 담기
        
        # 다음 숫자는 현재(i)보다 뒤에 있는 것만 고려함 (i + 1)
        comb(count + 1, i + 1)
        
        pick_numbers.pop() # 백트래킹 (되돌리기)

# 시작 인덱스를 0으로 주고 호출
comb(0, 0)


# 3234. 준환이의 양팔저울
'''
count : 뽑은 개수
# visited : 현재 뽑아놓은 상태
# left / right : 왼쪽과 오른쪽의 무게
'''
def dfs(count, visited, left, right):
     
    if count == N:
        return 1
     
    # 현재 방문 상태에서 left 무게를 이미 세었다면
    if dp[visited].get(left):
        return dp[visited][left]
     
    temp = 0
    for i in range(N):
        # i 번째 무게추를 골랐다면 건너뛰기
        if visited & (1 << i):
            continue
         
        temp += dfs(count+1, visited | (1 << i), left+weights[i], right)
        if left >= right+weights[i]:
            temp += dfs(count+1, visited | (1 << i), left, right+weights[i])
             
    # 현재 visited 상태에서 left 무게일 때의 경우의 수를 반환
    dp[visited][left] = temp
    return dp[visited][left]
     
'''
이렇게하면 시간초과
그래도 백트래킹의 흐름을 이해할 수 있는 좋은 코드임
'''
T = int(input())
 
for tc in range(1, T+1):
    N = int(input())
    weights = list(map(int, input().split()))
     
    dp = [{} for _ in range(2**N)]
     
    answer = dfs(0, 0, 0, 0)
    print(f'#{tc} {answer}')

def dfs(left_sum, right_sum, count):
    global ans
    if count == N:
        ans += 1
        return
    else:
        for i in range(N):   # 추 선택
            if visited[i] == 0:   # 아직 사용하지 않은 추이면
                visited[i] = 1    # 사용표시

                dfs(left_sum + W[i], right_sum, count + 1)   # 왼쪽에 올리는 경우

                if right_sum + W[i] <= left_sum:   # 오른쪽에 올리는 경우
                    dfs(left_sum, right_sum + W[i], count + 1)

                visited[i] = 0    # 사용해제


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    W = list(map(int, input().split()))

    visited = [0]*N
    ans = 0

    dfs(0, 0, 0)

    print(f'{tc} {ans}')   

