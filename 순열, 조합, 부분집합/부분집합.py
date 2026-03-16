# 부분집합

def recur(cnt, prev):
    print(path)

    for i in range(prev,len(H)):
        path.append(H[i])
        recur(cnt + 1, i + 1)
        path.pop()

H = [1,2,3,4,5]
path = []
recur(0,0)