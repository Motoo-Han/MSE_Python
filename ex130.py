#ex130
import requests #requests 사용하기 위해 모듈 추가!
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data'] #btc 변수에 할당! json 데이터 형식!
#사이트에서 가져올 수 있었던 정보들은?
변동폭 = float(btc['max_price']) - float(btc['min_price']) #얼마나 변동했을까?
시가 = float(btc['opening_price']) #시작 가격은?
최고가 = float(btc['max_price']) #최고가는?

if (시가+변동폭) > 최고가: #이때 (시가+변동가)의 금액이 최고가보다 높다면?
    print("상승장") #상승중! '상승장'을 출력하자.
else:               #만약 최고가보다 낮다면?
    print("하락장") #하락중! '하락장'을 출력하자.
