# 중복순열 > 중복이 가능하니까 방문표시가 필요하지 않음

path = []

def recur(cnt):

    if cnt == 2:
        print(path)
        return
    
    for i in range(4):
        path.append(i)
        recur(cnt + 1)
        path.pop()
        

# [0, 0]
# [0, 1]
# [0, 2]
# [0, 3]
# [1, 0]
# [1, 1]
# [1, 2]
# [1, 3]
# [2, 0]
# [2, 1]
# [2, 2]
# [2, 3]
# [3, 0]
# [3, 1]
# [3, 2]
# [3, 3]