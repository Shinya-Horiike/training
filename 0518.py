import random

print("おはよう. 会話をやめる時はESCと入力してくれ．")

while True:
    taiwa = input('> ')
    
    if taiwa == 'ESC':
        break

    ram = random.randint(1,3)

    if ram%3 == 0:
        print("なるほど. ")

    if ram%3 == 1:
        print("すごいな. ")

    if ram%3 == 2:
        print("悪いのは君じゃない. ")