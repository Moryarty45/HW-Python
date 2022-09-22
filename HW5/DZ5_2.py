from random import randint

print("Добро пожаловать в игру 'Конфеты 2021'")

player1 = "Игрок 1"
player2 = "Игрок 2"

def plays(x):
    if x == 1:
        playPlayer(drawPlayer)
    elif x == 2:
        playBot(drawPlayer)
    else:
        print(f"Нет такого режима!")
    return x

def draw():
    drawPlayer = randint(0,1)
    
    if drawPlayer:
        print(f"По итогам жеребьевки первым ходит игрок: {player1}")
    else:
        print(f"По итогам жеребьевки первым ходит игрок: {player2}")
    return drawPlayer

def playPlayer(drawPlayer):
    print(f"Игрок против игрока")
    valueCandy = 100
    while valueCandy > 27:
        if drawPlayer: 
            valueCandy -= playerTakeCandys(player1)
            drawPlayer = False
            print(f"На столе осталось: {valueCandy} конфет")
        else:
            valueCandy -= playerTakeCandys(player2)
            drawPlayer = True
            print(f"На столе осталось: {valueCandy} конфет")

    if drawPlayer:
        print(f"Выиграл игрок: {player1}")
    else:
        print(f"Выиграл игрок: {player2}")

def playBot(drawPlayer):
    print(f"Игрок против бота")
    valueCandy = 100
    while valueCandy > 27:
        if drawPlayer: 
            valueCandy -= playerTakeCandys(player1)
            drawPlayer = False
            print(f"На столе осталось: {valueCandy} конфет")
        else:
            botTakeCandys = randint(1,29)
            valueCandy -= botTakeCandys
            print(f"{player2} взял {botTakeCandys} конфет")
            drawPlayer = True
            print(f"На столе осталось: {valueCandy} конфет")

    if drawPlayer:
        print(f"Выиграл игрок: {player1}")
    else:
        print(f"Выиграл игрок: {player2}")

def playerTakeCandys(player):
    x = int(input(f"{player}, сколько конфет возьмете (от 1 до 28): "))
    while x < 1 or x > 28:
        x = int(input(f"{player}, взять можно только от 1 до 28: "))
    return x

drawPlayer = draw()
vs = int(input(f"Режим игры: 1. Игрок против игрока 2. Игрок против бота (введите 1 или 2): "))
plays(vs)