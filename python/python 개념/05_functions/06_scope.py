# Scope 예시
def func():
    num = 20
    print('local', num)  # local 20


func()

print('global', num)  # NameError: name 'num' is not defined


# 내장 함수 sum의 이름을 사용해버려서 오류가 발생하는 예시
print(sum)  # <built-in function sum>
print(sum(range(3)))  # 3
sum = 5
print(sum)  # 5
print(sum(range(3)))  # TypeError: 'int' object is not callable


# LEGB Rule 퀴즈  #local, enclosed, global, built-in (지역범위, 지역번위 한 단계 위 범위, 전역범위, 내장범위)
x = 'G'
y = 'G'


def outer_func():
    x = 'E'
    y = 'E'

    def inner_func(y):
        z = 'L'
        print(x, y, z)  # E, P, L

    inner_func('P')
    print(x, y)  # E, E


outer_func()
print(x, y)  # G, G