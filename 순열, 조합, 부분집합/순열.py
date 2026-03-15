# 순열 > 순서가 상괸이 있음.

path = []
visited = [0]*4

def recur(cnt):

    if cnt == 2:
        print(path)
        return
    
    for i in range(4):
        if visited[i] :
            continue
    
        visited[i] = 1
        path.append(i)
        recur(cnt + 1)
        path.pop()
        visited[i] = 0
        
recur(0)

# [0, 1]
# [0, 2]
# [0, 3]
# [1, 0]
# [1, 2]
# [1, 3]
# [2, 0]
# [2, 1]
# [2, 3]
# [3, 0]
# [3, 1]
# [3, 2]