import random
number = random.randint(1,100)

if(number%2==0):
    print("짝수입니다.")
else :
    print( "홀수입니다")

print(f"생성된 랜덤 정수 : {number}")