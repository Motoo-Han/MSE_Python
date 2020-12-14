#ex210
def message1(): #매세지1은 A를 출력한다!
    print("A") #라고 정의한다!

def message2(): #매세지2는 B를 출력한다!
    print("B") #라고 정의!

def message3(): #매세지3를 정의내리자.
    for i in range (3) : #0,1,2 세 번 반복동안,
        message2() #B출력을 진행한다.
        print("C") #그리고 C는 추가로 출력하자.
    message1() #마지막으로 A 추가!

message3() #깔끔!
