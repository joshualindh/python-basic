import random

your_credit = 3
computer_credit = 3

while(your_credit>0 and computer_credit>0) :
    number = random.randint(1,100)
    you = int(input("정수를 입력하세요."))

    if(number%2==you%2):
        print("당신이 이겼습니다")
        your_credit = your_credit+1
        computer_credit = computer_credit-1

    else :
        print("당신이 젔습니다")
        your_credit = your_credit-1
        computer_credit = computer_credit+1

    print(f"생성된 랜덤 정수 : {number}")
    print(f"당신의 크래딧은 {your_credit} 이고 컴퓨터의 크레딧은 {computer_credit}입니다.")
