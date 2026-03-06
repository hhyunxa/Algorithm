# 1545. 거꾸로 출력해 보아요
n = int(input())
for i in range(n, -1, -1) :
    print(i, end=' ')

# 1933. 간단한 N의 약수
n = int(input())
for i in range(1, n+1) :
    if n % i == 0 :
        print(i, end=' ')

# 2027. 대각선 출력하기
for i in range(5) :
    for j in range(5) :
        if i == j :
            print('#', end='')
        else :
            print('+', end='')
    print()

# 2071. 평균값 구하기
t = int(input())
for i in range(1, t+1) :
    n = list(map(int, input().split()))

    avg = sum(n) / 10
    result = int(avg + 0.5)
    print(f"#{i} {result}")

# 2058. 자릿수 더하기
n = int(input())
total = 0

while n > 0 :
    total += n % 10
    n = n // 10

print(total)

# 2019. 더블더블
n = int(input())
for i in range(n+1) :
    print(2**i, end =" ")
# (재귀함수 사용)
def double(a, n):
    if a > n:
        return
    print(2 ** a, end=' ')
    double(a + 1, n)

n = int(input())
double(0, n)
