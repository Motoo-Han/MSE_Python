#ex260
#에러의 원인이 무엇일까?
class OMG : 
    def print() : #여기 안에다가 self를 적자! 현재는 파라미터가 없다!
        print("Oh my god")

>>> >>> myStock = OMG()
>>> myStock.print() #이것은 print(mystock) 이랑 같은 취급이므로, 에러가 난다.
                    #따라서,self로 받아서 따로 처리해주어야 할 것이다. 
TypeError Traceback (most recent call last)
<ipython-input-233-c85c04535b22> in <module>()
----> myStock.print()

TypeError: print() takes 0 positional arguments but 1 was given
