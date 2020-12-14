#ex300
try:
    실행 코드
except:
    예외가 발생했을 때 수행할 코드
else:
    예외가 발생하지 않았을 때 수행할 코드
finally:
    예외 발생 여부와 상관없이 항상 수행할 코드
#예외처리가 가능하다고 한다..

per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i)) #try이므로, 무조건 시도하고, 오류가 뜬다면 except로 넘어간다!
    except:
        print(0) #오류가 안뜬다면 else로 넘어간다!
    else:
        print("clean data") #클린 데이타!
    finally: 
        print("변환 완료") #파이널리는 오류에 관계없이 항상 실행된다!
