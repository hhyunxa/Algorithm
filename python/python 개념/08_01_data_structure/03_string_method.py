################ 문자열 탐색 및 검증 ################

# find(x) : x의 첫 번째 위치를 반환. 없으면, -1을 반환.
text = 'banana'
print(text.find('a'))  # 1
print(text.find('z'))  # -1

# isupper() : 문자열 내의 모든 케이스 문자가 대문자인지 확인.
string1 = 'HELLO'
string2 = 'Hello'
print(string1.isupper())  # True
print(string2.isupper())  # False

# islower() : 문자열 내의 모든 케이스 문자가 소문자인지 확인.
print(string1.islower())  # False
print(string2.islower())  # False

# isalpha() : 문자열의 모든 문자가 알파벳이고 하나 이상의 문자가 포함되어 있으면 True를 반환. 단순 알파벳이 아닌 유니코드 상 Letter(한국어도 포함)
string1 = 'Hello'
string2 = '123heis98576ssh'
print(string1.isalpha())  # True
print(string2.isalpha())  # False


################ 문자열 조작 ################   # 문자열은 불변이니까

# replace(old, new[,count]) : 기존 문자열에서 "old"라는 부분 문자열이 "new"로 모두 바뀐 문자열을 반환
text = 'Hello, world! world world'
new_text1 = text.replace('world', 'Python')
new_text2 = text.replace('world', 'Python', 1)
print(new_text1)  # Hello, Python! Python Python
print(new_text2)  # Hello, Python! world world

# strip([chars]) : 선행과 후행 문자가 제거된 문자열의 복사본을 돌려줌.
# 사용자 입력 등에서 불필요한 공백이 포함된 경우
text = '   Hello    World   '

# 1. 아무것도 지정하지 않으면 '공백(띄어쓰기, 탭, 엔터)'을 제거
clean_text = text.strip()

print(clean_text)
# 결과: 'Hello    World'
# (주의: 문자열 중간의 공백은 제거되지 않음)


# 2. 제거할 문자를 지정하는 경우
text = '!!!Hello World!!!'
print(text.strip('!'))
# 결과: 'Hello World'


# [심화] 문자열 집합으로 제거 (순서 상관 없음)
# 'w', '.', 'c', 'o', 'm' 중 하나라도 양쪽 끝에 있으면 계속 제거
url = 'www.example.com'
print(url.strip('w.com'))
# 결과: 'example'
# (왼쪽의 'www.'과 오른쪽의 '.com'이 모두 제거됨)


# split(sep=None, maxsplit=-1) : sep를 구분자 문자열로 사용하여 문자열에 있는 단어들의 리스트를 반환.
# 1. 공백을 기준으로 분리 (기본 동작)
# - 여러 개의 공백도 하나로 처리하며, 앞뒤 공백은 무시함
text = '  Hello    Python  '
print(text.split())
# 결과: ['Hello', 'Python’]


# 2. 특정 문자를 기준으로 분리
# - 지정한 문자를 기준으로 '엄격하게' 분리함 (빈 문자열 발생 가능)
data = '10,20,,30'
print(data.split(','))
# 결과: ['10', '20', '', '30']


# 3. 분할 횟수 제한 (maxsplit)
# - 앞에서부터 1번만 자르고 나머지는 그대로 둠
path = 'User/admin/documents'
print(path.split('/', maxsplit=1))
# 결과: ['User', 'admin/documents']


# str.join(iterable) : 구분자로 iterable의 문자열을 연결한 문자열을 반환.
words = ['Python', 'is', 'awesome']

sentence1 = ' '.join(words)
sentence2 = '_'.join(words)

print(sentence1)  # Python is awesome
print(sentence2)  # Python-is-awesome


# capitalize() : 가장 첫 번째 글자를 대문자로 변경.
text = 'heLLo, woRld!'
new_text1 = text.capitalize()
print(new_text1)  # Hello, world!

# title() : 문자열 내 띄어쓰기를 기준으로 각 단어의 첫 글자는 대문자로, 나머지는 소문자로 변환.
new_text2 = text.title()
print(new_text2)  # Hello, World!

# upper() : 모두 대문자로 변경.
new_text3 = text.upper()
print(new_text3)  # HELLO, WORLD!

# lower() : 모두 소문자로 변경.
new_text4 = text.lower()
print(new_text4)  # hello, world!

# swapcase() : 대소문자로 서로 변경.
new_text5 = text.swapcase()
print(new_text5)  # HEllO, WOrLD!
