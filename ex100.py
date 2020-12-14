#ex100
date = ['09/05', '09/06', '09/07', '09/08', '09/09'] #data를 딕셔너리 close_table의 key로,
close_price = [10500, 10300, 10100, 10800, 11000] #close_price를 딕셔너리 close_table value로 해보자.

date = ['09/05', '09/06', '09/07', '09/08', '09/09'] #키
close_price = [10500, 10300, 10100, 10800, 11000] #값
close_table = dict(zip(date, close_price)) #으로 zip을 사용하여 딕셔너리 생성, 그리고 close_table로 지정한다.
print(close_table) #출력!
