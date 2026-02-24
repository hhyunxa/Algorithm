# 4828. [파이썬 S/W 문제해결 기본] 1일차 - min max
t = int(input())
for i in range(1, t+1):
    n = int(input())
    a = list(map(int, input().split()))
    result = max(a) - min(a)
    print(f'#{i} {result}')

# 4835. [파이썬 S/W 문제해결 기본] 1일차 - 구간합
t = int(input())
for i in range(1, t+1) :
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    
    result_sums = []
    for j in range(n-m+1) :
        sums = sum(a[j:j+m])
        result_sums.append(sums)
    result = max(result_sums) - min(result_sums)
    print(f'#{i} {result}')

# 16504. Gravity
T = int(input())

for tc in range(1, T+1):
    answer = 0
    N = int(input())
    boxes = list(map(int, input().split()))

    # 기준점 세팅
    for i in range(N):
        # 기준점으로부터 더 작은 박스 세어주기
        count = 0
        for j in range(i+1, N):
            if boxes[i] > boxes[j]:
                count += 1

            if answer < count:
                answer = count


    print(f'#{tc} {answer}')