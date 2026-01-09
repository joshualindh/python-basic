import random
game = 3
win = 0
lose = 0

while(game) :
    number = random.randint(1,100)

    while(True) :
        you = input("정수를 입력하세요.")
        if not you.isnumeric(  ) : #숫자가 아니라 숫자형 문자를 판별한다.
            print("정수가 아닙니다.")
            print("정수를 입력하세요.")
            continue
        break
    game = game-1 # 게임 횟수 차감

    you_number = int(you)

    if(number%2 ==you_number%2) :
        print("당신이 이겼습니다.")
        win = win + 1 #승리 횟수 증가

    else :
        print("당신이 졌습니다.")
        lose = lose + 1 #패배 횟수 증가

    print(f"생성된 랜덤 정수 :{number}")
    print(f"{win}승 {lose}패 입니다.") #현재까지 승패 기록 출력