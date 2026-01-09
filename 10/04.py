import random
game = 3 # 게임 횟수 설정

while(game) :
    number = random.randint(1,100) # 매 게임마다 새로운 랜덤 정수 생성

    while(True) :
        you = input("정수를 입력하세요.")
        if not you.isnumeric( ) : #숫자가 아니라 숫자형 문자를 판별한다.
            print("정수가 아닙니다.")
            print("정수를 입력하세요.")
            continue
        break
    game = game-1 # 게임 횟수 차감

    you_number = int(you) # 문자열을 정수형으로 변환

    if(number%2 ==you_number%2) :
        print("당신이 이겼습니다.")

    else :
        print("당신이 졌습니다.")

    print(f"생성된 랜덤 정수 :{number}") # 생성된 랜덤 정수 출력