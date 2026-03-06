# 123 입력 시
# "123" 로 저장
input_test = input()
print(input_test)

# 1 2 3 입력 시
# ['1', '2', '3'] 로 저장
input_test = input().split()
print(input_test)

# 1 2 3 입력 시
# [1, 2, 3] 로 저장
input_test = list(map(int, input().split()))
print(input_test)

# 1 2 3 입력 시 각각 배분
# a = 1 , b = 2 , c = 3
a, b, c = map(int, input().split())
print(a, b, c)

# 123 입력 시
# ['1', '2', '3'] 로 저장
input_test = list(input())
print(input_test)

# 123 입력 시 
# [1, 2, 3] 로 저장
input_test = list(map(int, input()))
print(input_test)

# 1 2 3
# 1 2 3
# 1 2 3  2차원 배열 입력 시
# [
#   [1,2,3],
#   [1,2,3],
#   [1,2,3]
# ]
# 와 같이 2차원 배열로 저장
input_test = [list(map(int, input().split())) for _ in range(3)]
print(input_test)

# 123
# 123
# 123  2차원 배열 입력 시
# [
#   [1,2,3],
#   [1,2,3],
#   [1,2,3]
# ]
# 와 같이 2차원 배열로 저장
input_test = [list(map(int, input())) for _ in range(3)]
print(input_test)