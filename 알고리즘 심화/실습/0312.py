# 1952. [모의 SW 역량테스트] 수영장
'''
DP로 풀기
DP : 부분문제를 바탕으로 전체문제를 해결한다.
'''
T = int(input())
for tc in range(1, T+1):
    day_fee, month_fee, quarter_fee, year_free = map(int, input().split())
    days = list(map(int, input().split()))

    dp = [0] * 13   # dp[i] > i월 까지 이용했을 때의 누적 최소 비용

    for i in range(1, 13):
        fee = dp[i-1] + (days[i-1] * day_fee)   # 일권
                                                # i = 4 > 3월까지의 누적최소비용 + 4월비용
        if fee > dp[i-1] + month_fee:   # 월권
            fee = dp[i-1] + month_fee

        if i >= 3:   # 3개월권  # 3월부터 3개월권이 의미있음
            if fee > dp[i-3] + quarter_fee:   # i = 4 > 1월까지의 누적최소비용 + 2, 3, 4월(3개월)비용
                fee = dp[i-3] + quarter_fee
        else:                  # 1, 2월은 이전 달이 없음
            if fee > quarter_fee:             # i = 2 > 1, 2, 3월용 3개월 비용
                fee = quarter_fee

        dp[i] = fee

    answer = dp[12]
    if answer > year_free:
        answer = year_free

    print(f'#{tc} {answer}')

'''
완탐으로 풀기
'''
def dfs(month, fee):
    global answer

    if fee >= answer:
        return

    if month >= 12:
        if answer > fee:
            answer = fee
        return
    
    # 일권
    dfs(month+1, fee + day_fee*days[month])
    # 월권
    dfs(month+1, fee + month_fee)
    # 3개월권
    dfs(month+3, fee + quarter_fee)

T = int(input())

for tc in range(1, T+1):
    day_fee, month_fee, quarter_fee, year_free = map(int, input().split())
    days = list(map(int, input().split()))

    answer = year_free
    dfs(0, 0)

    print(f'#{tc} {answer}')


# 1953. [모의 SW 역량테스트] 탈주범 검거
T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    