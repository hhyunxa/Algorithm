## 사용자 정의 모듈
import my_math

# from my_math import add

print(my_math.add(1, 2))
# print(add(1, 2))


## 사용자 정의 패키지
from my_package.math import my_math  # 마지막으로 정의된 걸로 덮어씌워짐
from my_package.statistics import tools

print(my_math.add(1, 2))  # 출력 : 3  # 마지막의로 정의된걸로 출력  # 되도록이면 as 사용
print(tools.mod(1, 2))  # 출력 : 1
