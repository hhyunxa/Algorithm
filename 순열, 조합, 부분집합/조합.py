# 조합

path = []
visited = [0]*4

def recur(cnt, prev):

    if cnt == 2:
        print(path)
        return
    
    for i in range(prev, 4):
        if visited[i]:
            continue

        visited[i] = 1
        path.append(i)
        recur(cnt + 1, i+1)
        path.pop()
        visited[i] = 0
        
recur(0,0)

# [0, 1]
# [0, 2]
# [0, 3]
# [1, 2]
# [1, 3]
# [2, 3]