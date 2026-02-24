# 강사님 ver.
import math

balls = [
    [30, 30]
    [-1, -1]
    [-1, -1]
    [10, 10]
    [-1, -1]
    [-1, -1]

]

whiteBall_y = balls[0][0]
whiteBall_x = balls[0][1]

for i in range(1, 6):
    if balls[i][0] >= 0:
        targetBall_y = balls[i][0]
        targetBall_x = balls[i][1]
        break

radian = math.atan2(targetBall_y-whiteBall_y, targetBall_x-whiteBall_x)
angle = math.degrees(radian)
power = 100
print(angle)


# 누군가 ver.
from math import atan2
import math


balls = [
    [1, 2], # white_ball
    [-1, -1],
    [124, 565], # target_ball
    [-1, -1],
    [-1, -1],
    [-1, -1]
]
# 위의 balls는 뭐 어떻게 알아서 나와있을듯


white_ball = balls[0] # = [1, 2]

for i in range(1, len(balls)):
    if balls[i][0] >= 0:
        target2_ball = balls[i] # = [124, 565]

radian = atan2(target2_ball[0] - white_ball[0], target2_ball[1] - white_ball[1])

angle = 180 / math.pi * radian

power = 100

'''
angle , power 설정하기
'''