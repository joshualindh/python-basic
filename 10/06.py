money = 1000000
dollar = 1146

dollar_100 = money//(dollar*100)
money_return = money%(dollar*100)

print(f"백달러 지폐는{dollar_100}장 입니다.")
print(f"돌려 받은 한화는{money_return}원 입니다.")
print(f"1dollar 는 {dollar}원 입니다.")