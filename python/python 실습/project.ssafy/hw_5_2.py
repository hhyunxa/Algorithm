# 아래 함수를 수정하시오.
def count_character(a,b):
    countt = 0
    for i in a :
        if i == b :
            countt = countt + 1
    return countt



result = count_character("Hello, World!", "o")
print(result)  # 2
