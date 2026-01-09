while(True) :
        money = input("환전할 금액을 입력하세요.")
        if not money.isnumeric(  ) : #숫자가 아니라 숫자형 문자를 판별한다.
            print("정수가 아닙니다.")
            print("정수를 입력하세요.")
            continue
        break
money = int(money)

while(True) :
        dollar = input("환율을 입력하세요.")
        if not dollar.isnumeric(  ) : #숫자가 아니라 숫자형 문자를 판별한다.
            print("정수가 아닙니다.")
            print("정수를 입력하세요.")
            continue
        break
dollar = int(dollar)

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