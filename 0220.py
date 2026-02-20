# 수업
# 전위순회
def pre_order(T) :
    if T:
        print(T)
        pre_order(left[T])
        pre_order(right[T])

# 중위순회
def in_order(T):
    if T:
        in_order(left[T])
        print(T, end = ' ')
        in_order(right[T])

# 후위순회
def post_order(T):
    if T:
        post_order(left[T])
        post_order(right[T])
        print(T, end = ' ')

V = int(input())  # 정점수. 1~V번 까지의 정점
E = V - 1
arr = list(map(int, input().split()))
# 부모를 인덱스로 자식 저장
left = [0] * (V + 1)
right = [0] * (V + 1)
# 자식을 인덱스로 부모 저장
par = [0] * (V + 1)
for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if left[p] == 0:  # 아직 자식이 없으면
        left[p] = c
    else:
        right[p] = c
    par[c] = p        # 자식을 인덱스로 부모를 저장

root = 1  # 루트를 1이라고 가정하고 루트 찾기
for i in range(1, V+1):
    if par[i] == 0:  # 부모가 없으면 root
        root = i
        break
    
pre_order(root)
print()
in_order(root)
print()
post_order(root)
print()

# heap
def enq(n):
    global last
    last += 1   # 마지막 정점 추가
    heap[last] = n   # 마지막 정점에 key 추가
    c = last
    p = c // 2   # 완전이진트리에서 부모 정점 번호
    while p and heap[p] < heap[c]:   # 부모가 있고, 부모 < 자식 인경우 자리 교환
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2

def deq():
    global last   # 완전 이진트리의 마지막 정점 번호
    tmp = heap[1]   # 삭제할 루트 원소 백업
    heap[1] = heap[last]   # 마지막 노드를 루트로 복사
    last -= 1   # 마지막 노드 삭제
    p = 1   # 루트가 부모
    c = p * 2   # 왼쪽 자식 번호(비교할 자식 번호)
    while c < last:   # 자식이 하나라도 있으면(왼쪽 자식이 있으면)
        if c+1 <= last and heap[c] < heap[c+1]:   # 오른쪽 자식이 있고 더 크면
            c += 1   # 비교할 대상을 오른쪽 자식으로
        if heap[p] < heap[c]:   # 자식이 더 크면 최대힙 규칙에 위배
            heap[p], heap[c] = heap[c], heap[p]
            p = c
            c = p // 2
        else :
            break
    return tmp

    

heap = [0] * 100   # 최대 99개의 데이터가 인큐된다고 가정. (99번 노드까지)
last = 0   # 완전 이진트리는 1번 정점부터 있으므로 아직 노드가 없는 상태
enq(2)
enq(5)
enq(7)
enq(3)
enq(4)
enq(6)
while last:
    print(deq())