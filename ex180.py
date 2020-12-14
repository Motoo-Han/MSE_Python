#ex180
low_prices  = [100, 200, 400, 800, 1000] #저가 리스트,
high_prices = [150, 300, 430, 880, 1000] #고가 리스트가 있다!

volatility = [ ] #보라틸리티(?) 리스트에 저장해보자.
for i in range(5): #0~4까지의 수가 i에 임할것이다.
    변동값 = high_prices[i] - low_prices[i] #늘 그렇듯 변동값은 고가-저가이다.
    volatility.append(변동값) #이 변동값을 보라틸리티 리스트에 추가하자.
print(volatility) #짜잔!
