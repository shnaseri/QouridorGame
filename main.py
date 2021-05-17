from Person import Person
from Wall import Wall
from Block import Block
blocks = []
def initmatrix():
    global blocks
    for i in range(10):
        for j in range(10):
            if i == 0 and j == 5:
                blocks.append(Block(i,j,'G'))
            elif i == 9 and j == 5:
                blocks.append(Block(i,j,'R'))
            else:
                blocks.append(Block(i,j))

initmatrix()
