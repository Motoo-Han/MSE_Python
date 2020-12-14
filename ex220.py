#ex220
def print_max(a, b, c) : #a,b,c 세 개의 파라미터를 가지는 함수를 정의하자!
    max_val = 0 #최대값 변수를 만들고, 0으로 할당!
    if a > max_val : #만약 a값이 최대값 변수보다 크다면
        max_val = a #최대값 변수를 a로 지정!
    if b > max_val : #만약 b값이 최대값 변수보다 크다면
        max_val = b #최대값 변수를 b로 지정!
    if c > max_val : #만약 c값이 최대값 변수보다 크다면
        max_val = c #최대값 변수를 c로 지정!
    print(max_val) #최대값을 출력하자!
print_max(3,4,8) #값 등장!
