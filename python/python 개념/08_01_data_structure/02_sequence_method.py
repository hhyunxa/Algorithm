# index(x) : 시퀀스에서 첫 번쨰로 일치하는 항목 x의 인덱스를 반환. 없으면, ValueError 발생.
text = 'banana'
print(text.index('a'))  # 1

my_list = [1, 2, 3]
print(my_list.index(2))  # 1


# count(x) : 시퀀스 s에서 등장하는 항목 x의 개수를 반환.
text = 'banana'
print(text.count('a'))  # 3

my_list = [1, 2, 2, 3, 3, 3]
print(my_list.count(3))  # 3
