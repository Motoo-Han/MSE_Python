#ex160
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py'] #리스트가 있다!
for i in 리스트: #변수를 i로, 리스트에서 검사해 보자!
    name, ext = i.split('.') #',' 를 기준으로 name과 ext로 나누어 보자. 이때 ext가 확장자이다!
    if ext == 'h' or ext == 'c': #만약 확장자인 b가 h거나 c라면,
        print(i) #그 파일을 출력해라! 
