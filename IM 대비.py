# 23569. 두개의 탑
T = int(input())
for tc in range(1, T+1) :
    A, N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    new_numbers = sorted(numbers, reverse=True)
    new_numbers_idx = 0
    hN, hM = 1, 1
    count = 0

    while hN <= N and hM <= M :
        count += new_numbers[new_numbers_idx] * hN
        new_numbers_idx += 1
        count += new_numbers[new_numbers_idx] * hM
        new_numbers_idx += 1
        hN += 1
        hM += 1

    while hN <= N :
        count += new_numbers[new_numbers_idx] * hN
        new_numbers_idx += 1
        hN += 1

    while hM <= M :
        count += new_numbers[new_numbers_idx] * hM
        new_numbers_idx += 1
        hM += 1

    print(f'#{tc} {count}')
