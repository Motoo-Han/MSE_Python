#ex030
string = 'abcd' #string이 abcd라고 지정
string.replace('b', 'B') #string의 b를 B로 대체
print(string) #그러나 string은 여전히 abcd
#B로 대체된 aBcd를 지정해주는 변수가 없다.
#즉 replace는 지정된 문자를 변환한뒤에 string변수를 반환한다.
#하지만 반환값을 string이 받은 것이 아니기에 string은 여전히 abcd이다.
#더욱이 문자열리스트는 값 수정이 불가능하다.
