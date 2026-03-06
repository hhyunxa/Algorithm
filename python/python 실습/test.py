# 사과는 영어로 apple
# 바나나는 영어로 banana
# 키위는 영어로 kiwi

apple = "사과는 영어로 apple "
banana = "바나나는 영어로 banana"
kiwi = "키위는 영어로 kiwi"
print(apple + '\n' + banana + '\n' + kiwi)

n = int(input())
for i in range(1, n+1) :
    if n % i == 0 :
        print(i, end=' ')


   