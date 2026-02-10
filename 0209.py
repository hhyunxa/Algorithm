# 4866. [파이썬 S/W 문제해결 기본] 4일차 - 괄호검사
T = int(input())
for tc in range(1, T+1) :
    N = input()

    stack = [0] * 100
    top = -1
    ans = 1

    for i in N :
        if i == '(' or i == '{' :
            top += 1
            stack[top] = i

        elif i == ')' or i == '}' :
            if top == -1 :
                ans = 0
                break
            
            if (i == ')' and stack[top] == '(') or (i == '}' and stack[top] == '{') :
                top -= 1
            else :
                ans = 0
                break

    if top != -1 :
        ans = 0

    print(f'#{tc} {ans}')


# 2005. 파스칼의 삼각형
T = int(input())
for tc in range(1, T+1) :
    N = int(input())

    arr = [[0] * N for _ in range(N)]

    for r in range(N) :
        for c in range(r+1) :
            if c == 0 :
                arr[r][c] = 1
            elif r == c :
                arr[r][c] = 1
            else :
                arr[r][c] = arr[r-1][c-1] + arr[r-1][c]

    print(f'#{tc}')
    for r in range(N) :
        for c in range(r+1) :
            print(arr[r][c], end = ' ')
        print()