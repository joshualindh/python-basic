import random

number = random.randint(1,100)
you = int(input("정수를 입력하세요. :"))

if(number%2==you%2):
    print("당신이 이겼습니다")
else :
    print("당신이 졌습니다")

print(f" 생성된 랜덤 정수 : {number}")
