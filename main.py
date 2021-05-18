from Person import Person
from Wall import Wall
from Block import Block

Persons = []


def initmatrix():
    for i in range(9):
        for j in range(9):
            blocktemp = Block(i, j)
            if i == 0 and j == 4:
                blocktemp.value = Person(blocktemp, 'G')
                Block.blocks.append(blocktemp)
                Persons.append(Person(blocktemp, 'G'))
            elif i == 8 and j == 4:
                blocktemp.value = Person(blocktemp, 'R')
                Block.blocks.append(blocktemp)
                Persons.append(Person(blocktemp, 'R'))
            else:
                Block.blocks.append(blocktemp)


def checkWin():
    if Persons[0].block.x == 8:
        print('Green is Winner.')
    elif Persons[1].block.x == 0:
        print('Red is Winner.')
    return
def print_board():
    for i in range(19):
        print('-',end='')
    print()
    wall_h = [wall for wall in Wall.walls if wall.orientation == 'H']
    wall_v = [wall for wall in Wall.walls if wall.orientation == 'V']

    for i in range(17):
        print('|', end='')
        if i % 2 == 0:
            for j in range(17):
                if j % 2 == 0:
                    block = [
                        block for block in Block.blocks if block.x == i//2 and block.y == j//2]
                    if len(block) != 0:
                        block = block[0]
                        if block.value is None:
                            print(0, end='')
                        else:
                            print(block.value.color, end='')
                else:
                    wall = [wall for wall in wall_v if wall.startX ==
                            i and wall.startY == j]
                    if len(wall) != 0:
                        print('|', end='')
                    else:
                        print(' ', end='')
        else:
            for j in range(17):
                if j % 2 == 0:
                    wall = [wall for wall in wall_h if wall.startX ==
                            i//2 and wall.startY == j//2]
                    if len(wall)==0:
                        print(' ',end = '')
                    else:
                        print('-', end='')
                else:
                    print(' ', end='')
        print('|')

    for i in range(19):
        print('-',end='')


def menu():
    print("""
    1 . Add Wall
    2 . Move
    3. exit to menu
    """)


turn = -1
initmatrix()
print(Block.blocks)
while True:
    print("""
    1 . startgame
    2 . exit
    """)
    startgame = int(input())

    if startgame == 1:
        print_board()
        while True:
            menu()
            if turn == -1:
                print('Green is your turn')
            else:
                print('Red is your turn')
            selectmenu = int(input())
            if turn == -1:
                index = 0
            else:
                index = 1
            if selectmenu == 1:
                function = input(
                    'Enter your func (\'startx starty H/V \') : ').split()
                walltemp = Wall(int(function[0]), int(function[1]), function[2])
                if Persons[index].AddWall(walltemp):
                    turn *= -1
                    print('Add wall is successful')
                else:
                    print('Unsuccessful')
            elif selectmenu == 2:
                jahat = input('Enter yout Direction (U/D/R/L) : ')
                if Persons[index].move(jahat, Block.blocks):
                    turn *= -1
                    print('Move is Successful')
                else:
                    print('Unsuccessful.')
            else:
                break
            if checkWin():
                exit(0)
            print_board()

    else:
        exit(0)
