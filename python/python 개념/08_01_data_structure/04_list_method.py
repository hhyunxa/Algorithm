################ 리스트 값 추가 및 삭제 ################

# append(x) : 리스트 마지막에 항목 x를 추가.
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # [1, 2, 3, 4]
# append는 None을 반환합니다.
print(my_list.append(4))  # None

# extend(iterable) : iterable의 모든 항목들을 리스트 끝에 추가(+=과 같은 기능).
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list)  # [1, 2, 3, 4, 5, 6]

# extend와 append의 비교
my_list.append([5, 6, 7])
print(my_list)  # [1, 2, 3, 4, 5, 6, [5, 6, 7]]

# my_list.extend(100)  # TypeError: 'int' object is not iterable

# insert(i, x) : 리스트 인덱스 i에 항목 x를 삽입.
my_list = [1, 2, 3]
my_list.insert(1, 5)
print(my_list)  # [1, 5, 2, 3]

# remove(x) : 리스트 가장 왼쪽에 있는 항목(첫 번째) x를 제거. 항목이 존재하지 않을 경우, ValueError.
my_list = [1, 2, 3, 2, 2, 2]
my_list.remove(2)
print(my_list)  # [1, 3, 2, 2, 2]

# pop() : 리스트 가장 오른쪽에 있는 항목(마지막)을 반환 후 제거.
# pop(i) : 리스트의 인덱스 i에 있는 항목을 반환 후 제거.
my_list = [1, 2, 3, 4, 5]
item1 = my_list.pop()
item2 = my_list.pop(0)

print(item1)  # 5
print(item2)  # 1
print(my_list)  # [2, 3, 4]

# clear() : 리스트의 모든 항목 제거.
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # []


################ 리스트 정렬 및 순서 변경 ################

# reverse() : 리스트의 순서를 역순으로 변경(정렬 X).
my_list = [1, 3, 2, 8, 1, 9]
my_list.reverse()
# reverse는 None을 반환합니다.
# print(my_list.reverse())  # None
# reverse는 원본 리스트를 변경합니다.
print(my_list)  # [9, 1, 8, 2, 3, 1]

# sort() : 리스트를 정렬(매개변수 이용가능).  # sorted()는 내장함수  sort는 리스트 전용
my_list = [3, 2, 100, 1]
my_list.sort()
# sort는 None을 반환합니다.
# print(my_list.sort())  # None
# sort는 원본 리스트를 변경합니다.  # sorted는 원본 리스트는 그대로 -> 원본 보면 됨. -> return필요 없음. #####################################################
# 즉 None이면 원본이 변경되는거임.
print(my_list)  # [1, 2, 3, 100]

# sort(내림차순 정렬)
my_list.sort(reverse=True)
print(my_list)  # [100, 3, 2, 1]
