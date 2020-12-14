#ex070
#첫번째 방법
data = [2, 4, 1, 3, 11, 5, 10, 9] #리스트이다.
data.sort() #sort는 원본 자체를 바꾸는 함수이다. 따라서 data는 정렬되었다.
print(data) #정렬된 data.

#두번째 방법
data = [2, 4, 1, 3, 11, 5, 10, 9] #마찬가지로 리스트이다.
data1 = sorted(data) #sorted는 원본 data를 정렬하여 data1에 지정한다.
print(data1) #정렬된 data1
