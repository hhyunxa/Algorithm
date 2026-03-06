# 아래 클래스를 수정하시오.
class StringRepeater:
    def repeat_string(self, count, string) :
        for  _ in range(count) :
            print(string)



repeater1 = StringRepeater()
repeater1.repeat_string(3, "Hello")
