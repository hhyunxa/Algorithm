# 아래 함수를 수정하시오.
def find_min_max(numbers):
    minn = numbers[0]
    maxx = numbers[0]
    for i in numbers :
        if minn > i :
            minn = i
        elif maxx < i :
            maxx = i
    return minn, maxx




result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)
