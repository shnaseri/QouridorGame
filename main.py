from Person import Person
from Wall import Wall
from Block import Block


def initmatrix():
    for i in range(10):
        for j in range(10):
            if i == 0 and j == 5:
                Block.blocks.append(Block(i, j, 'G'))
            elif i == 9 and j == 5:
                Block.blocks.append(Block(i, j, 'R'))
            else:
                Block.blocks.append(Block(i, j))


initmatrix()


def menu():
    print("""
    1 . Add Wall
    2 . Move
    3. exit to menu
    """)


turn = -1

while True:
    print("""
    1 . startgame
    2 . exit
    """)
    startgame = int(input())

    if startgame == 1:
        menu()
        if turn == -1:
            print('Green is your turn')
        else:
            print('Red is your turn')
        selectmenu = int(input())
        if selectmenu == 1:
            pass
            if True:
                turn *= -1
        elif selectmenu == 2:
            pass
            if True:
                turn *= -1
        else:
            break
    else:
        exit(0)
