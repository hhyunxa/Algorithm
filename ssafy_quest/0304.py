# 1001. A-B
A, B = map(int, input().split())
print(A-B)


# 27323. 직사각형
A = int(input())
B = int(input())
print(A*B)


# 27886. 문자와 문자열
S = input()
i = int(input())
print(S[i-1])


# 28113. 정보섬의 대중교통
N, A, B = map(int, input().split())
if A < B:
    print('Bus')
elif A > B:
    print('Subway')
else:
    print('Anything')


# 3003. 킹, 퀸, 룩, 비숍, 나이트, 폰
a, b, c, d, e, f = map(int, input().split())
A, B, C, D, E, F = 1, 1, 2, 2, 2, 8
print(A-a, B-b, C-c, D-d, E-e, F-f)