# 1.
T = int(input())
for tc in range(1, T+1):
    a = input()
    ans = '0'

    for i in a:
        if i == '.':
            ans += '0'

        elif i == '-':
            ans += '1'

    b = format(int(ans, 2), 'X')

    print(f'#{tc} {b}')
    

# 2.
def dfs(start, sum_w, sum_v):
    global max_v
    w, v = w_v_info[start]

    # 현재 방의 보물 챙기기
    if sum_w + w <= K:
        new_w = sum_w + w
        new_v = sum_v + v
        # 막다른 길인지 확인
        if len(adj[start]) == 0:
            if new_v > max_v:
                max_v = new_v
        else:
            for next in adj[start]:
                dfs(next, new_w, new_v)
    # 무게 초과 시 보물은 모두 사라짐
    else:
        pass
        
    # 현재 방의 보물 안챙기기
    if sum_w <= K:
        # 막다른 길인지 확인
        if len(adj[start]) == 0:
            if sum_v > max_v:
                max_v = sum_v
        else:
            for next in adj[start]:
                dfs(next, sum_w, sum_v)

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())

    cave = []
    start = 0
    adj = [[] for _ in range(N+1)]   # 자식 노드 번호를 담을 리스트
    w_v_info = [0] * (N+1)   # 방 번호를 인덱스로 무게와 가치 저장

    for _ in range(N):
        r, w, v, p = map(int, input().split())
        cave.append((r, w, v, p))
        w_v_info[r] = (w, v)

        if p == 0:
            start = r
        else:
            adj[p].append(r)

    max_v = 0
    dfs(start, 0, 0)

    print(f'#{tc} {max_v}')


# 공부
'''
2진수 16진수 변환, 대문자 변환 (내장함수 사용 가능)
2진수(문자열) > 10진수 > 16진수 > upper 
hex(int('31ndfDK103a1321', 2))
16진수 > 2진수 (bin)
2진수(문자열) > 10진수 > 16진수 > 대문자(X), 소문자(x)
                       8진수 > O, o
format(int('31ndfDK103a1321', 2), 'X')

완전탐색, 부분집합의 합(SWEA 4837), 장훈이의 높은 선반(SWEA 1486)

조건명제, 공허한 증명/자명한 증명/대우에 의한 증명 이해하기, 기초수식(과제)
공허한 증명 : p가 F일 때 > q의 참거짓에 상관 없이 전체명제는 항상 T
자명한 증명 : q가 T일 때 > p의 참거짓에 상관 없이 전체명제는 항상 T
대우에 의한 증명 : 위를 반대로 > p -> q == ~q -> ~p
기초수식 : p.81~, 문제 1 ~ 4

:warning: 서술형에서 감점이 많이 발생하고 있으므로 충분히 준비하기 바랍니다.
'''
# 1.
# 2진수 > 16진수
ans = format(int('11011010', 2), 'X')
print(ans)
# 16진수 > 2진수
ans = bin(int('DA', 16))
print(ans)

# 2.
def dfs(idx, sum_h):
    global ans
    if idx == N:
        if sum_h >= B:
            if ans > sum_h:
                ans = sum_h
        return
    
    dfs(idx + 1, sum_h + H[idx])   # 이번 점원 포함

    dfs(idx + 1, sum_h)   # 이번 점원 미포함

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))

    ans = 99999999
    dfs(0, 0)
    print(f'#{tc} {ans - B}')

# 3
'''
p -> q
공허한 증명 : p가 F일 때 > q의 참거짓에 상관 없이 전체명제는 항상 T
자명한 증명 : q가 T일 때 > p의 참거짓에 상관 없이 전체명제는 항상 T
대우에 의한 증명 : 위를 반대로 > p -> q == ~q -> ~p

만약 0이 홀수라면, 미국에서 2080년 월드컵이 열린다.
역 : 만약 미국에서 2080년 월드컵이 열린다면, 0이 홀수이다.
이 : 만약 0이 짝수라면, 미국에서 2080년 월드컵이 열리지 않는다.
대우 : 만약 미국에서 2080년 월드컵이 열리지 않는다면, 0은 짝수이다.
'''