import random
number = random.randint(1,100)

while(True) :
    you = input("정수를 입력하세요.") # 사용자에게 정수 입력 받기

    if not you.isnumeric(  ) : #숫자가 아니라 숫자형 문자를 판별한다.
        print("정수가 아닙니다.")
        print("정수를 입력하세요.")
        continue
    break

you_number = int(you)

if(number%2 ==you_number%2) :
    print("당신이 이겼습니다.")

else :
    print("당신이 졌습니다.")

print(f"생성된 랜덤 정수 :{number}")
