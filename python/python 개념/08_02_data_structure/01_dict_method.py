# D.get(k) : 키 k에 연결된 값을 반환. (키가 없으면 None을 반환)
# D.get(k, v) : 키 k에 연결된 값을 반환하거나 키가 없으면 기본 값으로 v를 반환.
person = {'name': 'Alice', 'age': 25}
print(person.get('name'))
print(person.get('country'))
print(person.get('country', 'Unknown'))
# print(person['country'])  # KeyError: 'country'  # get은 에러가 발생 안함. None을 반환함.

# D.keys() : 딕셔너리 D의 키를 모은 객체를 반환.
person = {'name': 'Alice', 'age': 25}
print(person.keys())  # dict_keys(['name', 'age'])
for item in person.keys():
    print(item)

# D.values() : 딕셔너리 D의 값을 모은 객체를 반환.
person = {'name': 'Alice', 'age': 25}
print(person.values())  # dict_values(['Alice', 25])
for item in person.values():
    print(item)

# D.items() : 딕셔너리 D의 키/값 쌍을 모은 객체를 반환.
person = {'name': 'Alice', 'age': 25}
print(person.items())  # dict_items([('name', 'Alice'), ('age', 25)])
for key, value in person.items():
    print(key, value)

# D.pop(k) : 딕셔너리 D에서 키 K를 제거하고 연결했던 값을 반환. (없으면 오류)
# D.pop(k, v) : 딕셔너리 D에서 키 K를 제거하고 연결했던 값을 반환. (없으면 v를 반환)
person = {'name': 'Alice', 'age': 25}
print(person.pop('age'))  # 25
print(person)  # {'name': 'Alice'}
print(person.pop('country', None))  # None
# print(person.pop('country'))  # KeyError: 'country'

# D.clear() : 딕셔너리 D의 모든 키/값 쌍을 제거.
person = {'name': 'Alice', 'age': 25}
person.clear()
print(person)

# D.setdefault(k) : 딕셔너리 D에서 키 K와 연결된 값을 반환.
# D.setdefault(k, v) : 딕셔너리 D에서 키 k와 연결된 값을 반환. k가 D의 키가 아니면 값 ㅍ와 연결한 키 k를 D에 추가하고 v를 반환.
person = {'name': 'Alice', 'age': 25}
print(person.setdefault('country', 'KOREA'))  # KOREA
print(person)  # {'name': 'Alice', 'age': 25, 'country': 'KOREA'}

# D.update(other) : other 내 각 키에 대해 D에 있는 키면 D에 있는 그 키의 값을 other에 있는 값으로 대체. other에 있는 각 키에 대해 D에 없는 키면 키/값 쌍을 D에 추가.
person = {'name': 'Alice', 'age': 25}
other_person = {'name': 'Jane', 'country': 'KOREA'}

person.update(other_person)
print(person)  # {'name': 'Jane', 'age': 25, 'country': 'KOREA'}

person.update(age=100, address='SEOUL')
print(
    person
)  # {'name': 'Jane', 'age': 100, 'country': 'KOREA', 'address': 'SEOUL'}
