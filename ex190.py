#ex190
apart = [ [101, 102], [201, 202], [301, 302] ] #리스트에 아파트 호수가 있다!
for i in apart: #아파트의 호수들을 i에 소환! 
    for home in i: #세분화된 리스트를 또다시 home에 소환!
        print(home, "호") #깔끔하게 '호' 를 붙여주자.
print("-----") #마무리!
