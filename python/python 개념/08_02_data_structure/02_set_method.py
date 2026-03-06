# s.add(x) : 세트 s에 항목 x를 추가. 이미 x가 있다면 변화 없음.
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.add(4)
print(my_set)

my_set.add(4)
print(my_set)

# s.update(iterable) : 세트 s에 다른 iterable 요소를 추가.
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.update([1, 4, 5])
print(my_set)  # {'c', 2, 3, 1, 'b', 4, 5, 'a'}

# s.clear() : 세트 s의 모든 항목을 제거.
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.clear()
print(my_set)  # set()

# s.remove(x) : 세트 s에서 항목 x를 제거. 항목 x가 없을 경우 Key error.
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.remove(2)
print(my_set)
# my_set.remove(10)  # KeyError: 10

# s.pop() : 세트 s에서 임의의 항목을 변환하고, 해당 항목을 제거.  # 임의의 인거지 또 완전 랜덤은 아님.
my_set = {'a', 'b', 'c', 1, 2, 3}
element = my_set.pop()
print(element)
print(my_set)

# s.discard(x) : 세트 s에서 항목 x를 제거. remove와 달리 에러가 없음.
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.discard(2)
print(my_set)
my_set.discard(10)

# 집합 메서드
set1 = {0, 1, 2, 3, 4}
set2 = {1, 3, 5, 7, 9}
set3 = {0, 1}

print(set1.difference(set2))  # {0, 2, 4}  # set1 - set2
print(set1.intersection(set2))  # {1, 3}  # set1 & set2
print(set1.issubset(set2))  # False  # set1 <= set2
print(set3.issubset(set1))  # True  
print(set1.issuperset(set2))  # False  # set1 >= set2
print(set1.union(set2))  # {0, 1, 2, 3, 4, 5, 7, 9}  # set1 | set2
