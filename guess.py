import random
import os
import time


class gamble :
    def __init__ (self, low, high):
        self.low = low
        self.high = high
        self.guess = (low+high) // 2
        self.chance = 1

    def when_its_low(self):
        make_log(f'{self.guess} is lower. Chance left : {7 - self.chance}')
        self.low =self.guess + 1
        self.guess = (self.low + self.high) // 2
        self.chance += 1

    def when_its_high(self):
        make_log(f'{self.guess} is bigger. Chance left : {7 - self.chance}')
        self.high = self.guess - 1
        self.guess = (self.low + self.high) // 2
        self.chance += 1


log_write = []


def make_log(a) :
    global log_write  # 전역변수는 쓰기 전에 이렇게 쓰는 게 맞다고 함, = 연산자와 함께 쓰이지 못함 by chat gpt
    print(a)
    a += "\n"
    log_write.append(a)


dir_name = "C:\\202444085_Assemble\\KSEB_2025\\Python\\2025_KEB_datastructure_algorithm"
filename = "guess.txt"
fullname = os.path.join(dir_name, filename)

while True :
    if not os.path.isfile(fullname) :
        with open(fullname, 'w') as fp:
            fp.write("gamble log\n")
            fp.write("*"*30)
            fp.write('\n')
            pass
    else :
        with open(fullname, 'a') as fp:
            game_count = 1

            while True :
                game = gamble(0,100)
                decorate = ""
                if game_count % 10 == 1:
                    decorate = "1st try"
                elif game_count % 10 == 2:
                    decorate = "2nd try"
                elif game_count % 10 == 3:
                    decorate = "3rd try"
                else:
                    decorate = f"{game_count}th try"
                make_log(decorate)
                answer = random.randint(1, 100)
                make_log(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n')  # 문자열로 변환하고 줄안바꾸면 가독성 나빠짐

                while game.chance <= 7:
                    if game.guess == answer:
                        make_log(f'You win. Answer is {answer}')
                        break
                    elif game.guess > answer:
                        game.when_its_high()
                    else:
                        game.when_its_low()
                else:
                    make_log(f'You lost. Answer is {answer}')

                select = input("Wanna Continue ? (Y/N) : ").strip().upper()
                if select == 'Y' :
                    game_count += 1
                    make_log('\n')
                    continue
                else :
                    make_log('\n')
                    break
            if select != 'Y' :
                for log in log_write :
                    fp.write(log)
                fp.write("*" * 30)
                fp.write("\n")
                break



