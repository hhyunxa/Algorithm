# 2112. [모의 SW 역량테스트] 보호 필름
def test_film():
    # 통과 시 True
    # 실패 시 False 
    for c in range(W):
        count = 0
        before = -1
        for r in range(D):
            if films[r][c] != before:
                count = 1
            else :
                count += 1
                if count >= K:
                    break
            before = films[r][c]
        if count < K:
            return False
    return True

def comb(count, idx):
    global answer
    
    if test_film():
        answer = count

    if count >= answer-1:
        return
    
    for i in range(idx, D):
        backup = films[i]
        films[i] = A
        comb(count+1, i+1)
        films[i] = B
        comb(count+1, i+1)
        films[i] = backup

T = int(input())
A = [0]*20
B = [1]*20

for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    films = [list(map(int, input().split())) for _ in range(D)]
    answer = K

    comb(0, 0)

    print(f'#{tc} {answer}')