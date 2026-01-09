money = int(input("환전할 금액을 입력하세요"))
dollar =  int(input("환율을 입력하세요"))

dollar_100 = money//(dollar*100)
money_return = money%(dollar*100)

dollar_10 = money_return//(dollar*10)
money_return = money_return%(dollar*10)

dollar_5 = money_return//(dollar*5)
money_return = money_return%(dollar*5)

dollar_1 = money_return//dollar
money_return = money_return%dollar


print(f"백달러 지폐는{dollar_100}장 입니다.")
print(f"십달러 지폐는{dollar_10}장 입니다.")
print(f"오달러 지폐는{dollar_5}장 입니다.")
print(f"일달러 지폐는{dollar_1}장 입니다.")
print(f"돌려 받은 한화는{money_return}원 입니다.")