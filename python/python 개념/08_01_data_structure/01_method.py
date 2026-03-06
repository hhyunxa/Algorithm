# 메서드 : 객체가 가진 함수, 메서드는 클래스 내부에 정의되는 함수

# 클래스는 파이썬에서 '타입을 표현하는 방법'이며 이미 은연중에 사용해왔음.
print(type('1'))  # <class 'str'>
print(type([1, 2]))  # <class 'list'>
# print(help(str))
# print(help(list))


# 함수
def append():
    pass


# 함수 호출
append()


# 메서드 호출
리스트.append()
객체.메서드()


# 문자열 메서드 예시
print('hello'.capitalize())  # Hello

# 리스트 메서드 예시
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)  # [1, 2, 3, 4]
