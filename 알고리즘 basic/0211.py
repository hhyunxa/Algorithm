# 수업
# 중위표기법 -> 후위표기법
stack = [0] * 100
top = -1

icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}
isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}

infix = '(6+5*(2-8)/2)'
postfix = ''

for token in infix:
    # 1. 피연산자(숫자 등)인 경우
    if token not in '(+-*/)':
        postfix += token
    
    # 2. 닫는 괄호인 경우
    elif token == ')':
        while top > -1 and stack[top] != '(':
            postfix += stack[top] # pop
            top -= 1
        top -= 1 # '('를 스택에서 버림
        
    # 3. 연산자 및 여는 괄호인 경우
    else:
        # 스택이 비었거나, 토큰의 우선순위가 더 높으면 push
        if top == -1 or isp[stack[top]] < icp[token]:
            top += 1
            stack[top] = token
        # 토큰의 우선순위가 낮거나 같으면 높을 때까지 pop
        else:
            while top > -1 and isp[stack[top]] >= icp[token]:
                postfix += stack[top]
                top -= 1
            top += 1
            stack[top] = token

# 마지막으로 스택에 남은 연산자들 처리
while top > -1:
    postfix += stack[top]
    top -= 1

print(postfix)


# 실습
# 1222. [S/W 문제해결 기본] 6일차 - 계산기1 
T = 10
for tc in range(1, T+1) :
    lens = int(input())
    strs = input()

    # 후위 연산으로 바꾸기
    answer = ''
    stack = [0] * lens
    top = -1
   
    for token in strs :
        if token != '+' :   # 숫자면 answer에 바로 저장
            answer += token
        
        else :              # '+'면 
            while top > -1 and stack[top] == '+' :
                answer += stack[top]   # pop
                top -= 1
            top += 1                   # pop 끝나면 push
            stack[top] = token

    while top > -1 :
        answer += stack[top]
        top -= 1

    # 후위연산 계산하기 (숫자는 push 연산을 만나면 pull 해서 연산하기)
    stack2 = [0] * len(answer)
    top2 = -1

    for token2 in answer :
        if token2 != '+' :
            top2 += 1                 # 숫자면 push
            stack2[top2] = int(token2)

        else :                        # '+'면 pop
            a = stack2[top2]
            top2 -= 1
            b = stack2[top2]
            top2 -= 1

            top2 += 1                # 두개의 합 push
            stack2[top2] = a + b

    print(f'#{tc} {stack2[top2]}')


# 2806. N-Queen
def n_queen(r) :
    global answer

    if r == N :
        answer += 1
        return
    
    for c in range(N) :
        # 위쪽 검사
        if c in visited :
            continue

        # 위쪽 대각 검사
        for test_r in range(r) :
            if r-test_r == abs(c-visited[test_r]) :
                break
        else :
            visited[r] = c
            n_queen(r+1)
            visited[r] = -1

T = int(input())
for tc in range(1, T+1) :
    N = int(input())

    answer = 0
    # -1은 미방문 상태 > 해당 행에 대해서 뽑지 않았음
    visited = [-1] * N

    # 0번부터 뽑기 시작
    n_queen(0)
    
    print(f'#{tc} {answer}')