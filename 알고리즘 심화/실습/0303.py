# 5644. [모의 SW 역량테스트] 무선 충전
'''
dr, dr > 방향이동
T > TC 수
M > 이동횟수
N > 배터리의 수
A, B > 각각 A, B 이동경로(델타의 인덱스)
human_rcs > A(0), B(1) 좌표
BC_info > 배터리의 정보(N개)
charge_idxs > (0)A가 충전할 수 있는 위치 인덱스 모음
             (1)B가 충전할 수 있는 위치 인덱스 모음

1. 이동 > M번 
    2. 이동한 위치에서 A, B 충전할 수 있는 충전소 파악
        - A, B 충전소 간의 거리를 파악 > 해당 거리가 충전 범위 이내이면 충전 가능
    3. 최적의 충전량을 고르기 > max
        ㄱ. A만 충전할 수 없는 경우
            > B를 반복
        ㄴ. B만 충전할 수 없는 경우
            > A를 반복 
        ㄷ. A, B 둘 다 충전 가능한 경우
    4. max 누적
'''
#        상  우  하  좌
dr = [0, 0, 1, 0, -1]
dc = [0, -1, 0, 1, 0]
 
T = int(input())
 
for tc in range(1, T+1):
    answer = 0
    # M 이동횟수, N 배터리 수
    M, N = map(int, input().split())
    # A, B 이동 정보(매초마다 이동방향)
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # A, B 좌표
    human_rcs = [[1, 1],[10, 10]]
    # 배터리 정보((좌표), 충전 범위, 충전량)
    BC_info = [0]*N
    for i in range(N):
        BC_info[i] = list(map(int, input().split()))
     
    # 충전 > M + 1
    for time in range(M+1):
        # 충전 가능한 위치 탐색 - A, B
        charge_idxs = [[], []]
        # A, B 둘 중 누구를 돌지 > 0/1
        # i: A인지 B인지
        for i in range(2):
            r, c = human_rcs[i]
            # 어떤 충전소인지 선택
            # j: 충전소 번호
            for j in range(N):
                BC_r, BC_c, coverage, charge_amount = BC_info[j]
                if abs(r-BC_r) + abs(c-BC_c) <= coverage:
                    charge_idxs[i].append(j)
 
        # 최적 충전량 - ㄱ, ㄴ, ㄷ
        charge = 0
        # ㄱ. A가 충전할 수 없는 경우
        if not charge_idxs[0]:
            for i in charge_idxs[1]:
                if BC_info[i][3] > charge:
                    charge = BC_info[i][3]
 
        elif not charge_idxs[1]:
            for i in charge_idxs[0]:
                if BC_info[i][3] > charge:
                    charge = BC_info[i][3]
        else:
            # i: A의 충전소 번호
            for i in charge_idxs[0]:
                # j: B의 충전소 번호
                for j in charge_idxs[1]:
                    if i == j:
                        if BC_info[i][3] > charge:
                            charge = BC_info[i][3]
                    else:
                        if BC_info[i][3] + BC_info[j][3] > charge:
                            charge = BC_info[i][3] + BC_info[j][3]
         
        answer += charge
 
        # 이동
        if time == M:
            break
         
        human_rcs[0][0] += dr[A[time]]
        human_rcs[0][1] += dc[A[time]]
 
        human_rcs[1][0] += dr[B[time]]
        human_rcs[1][1] += dc[B[time]]
 
    print(f'#{tc} {answer}')