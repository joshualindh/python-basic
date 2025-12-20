money = int(input("환전할 금액을 입력하세요 : "))

m_50000 = money//50000 ; money_changes = money%50000
m_10000 = money_changes//10000 ; money_changes = money%10000
m_5000 = money_changes//5000 ; money_changes = money%5000
m_1000 = money_changes//1000 ; money_changes = money%1000

print("오만원 : %d 장 " %m_50000)
print("만원 : %d 장 " %m_10000)
print("오천원 : %d 장 " %m_5000)
print("천원 : %d 장 " %m_1000)
print("지폐를 뺀 나머지 돈  : %d 원  " %money_changes)