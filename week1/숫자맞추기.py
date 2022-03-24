'''숫자 맞추기 게임 만들기
1부터 100까지의 임의의 수를 생성하고 생성된 임의의 수를 맞추는 게임 프로그램으로 
숫자를 하나 입력하면 임의로 생성된 수보다 높은지 정답인지를 알려준다.
정답을 맞힌 경우 정답을 몇 번 만에 맞추었는지 그 결과로 게임의 승부를 알 수 있다.'''

import random

random_number = random.randint(1, 100)

game_count = 1

while True:
    try:
        my_number = int(input("1~100 사이의 숫자를 입력하세요: "))

        if my_number > random_number:
            print("다운")
        elif my_number < random_number:
            print("업")
        elif my_number == random_number:
            print(f"축하합니다.{game_count}회 만에 맞췄습니다.")
            break

        game_count = game_count + 1
    except:
        print("에러가 발생하였습니다. 숫자를 입력하세요.")
