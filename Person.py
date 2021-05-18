from Wall import Wall


class Person:
    persons = []

    def __init__(self, block, color):
        self.block = block
        self.color = color
        self.wallsRemain = 10

    def AddWall(self, wall):
        if Wall.isValid(self, wall):
            Wall.walls.append(wall)
            if wall.orientation == 'H':
                Wall.walls.append(Wall(wall.startX, wall.startY + 1, 'H'))
            else:
                Wall.walls.append(Wall(wall.startX + 1, wall.startY, 'V'))
            self.wallsRemain -= 10
            return True
        else:
            return False

    def wallOk(self, jahat, jump):
        if jahat == 'l':
            if Wall.hasWall(Wall(self.block.x, self.block.y - 1, 'V')):
                return False
            if jump:
                if Wall.hasWall(Wall(self.block.x, self.block.y - 2, 'V')):
                    return False
        elif jahat == 'r':
            if Wall.hasWall(Wall(self.block.x, self.block.y, 'V')):
                return False
            if jump:
                if Wall.hasWall(Wall(self.block.x, self.block.y + 1, 'V')):
                    return False
        elif jahat == 'u':
            if Wall.hasWall(Wall(self.block.x - 1, self.block.y, 'H')):
                return False
            if jump:
                if Wall.hasWall(Wall(self.block.x - 2, self.block.y, 'H')):
                    return False
        elif jahat == 'd':
            if Wall.hasWall(Wall(self.block.x, self.block.y, 'H')):
                return False
            if jump:
                if Wall.hasWall(Wall(self.block.x + 9, self.block.y, 'H')):
                    return False
        return True

    def moveValid(self, jahat, blocks):
        blockList = self.block.getBlocks(jahat)
        jump = False
        if len(blockList) == 0:
            return (False)
        if len(blockList) == 1:
            if blockList[0].value != None:
                return (False)
            if not self.wallOk(jahat, False):
                return (False)
        if len(blockList) == 2:
            if blockList[0].value != None and blockList[1].value != None:
                return (False)
            if not self.wallOk(jahat, True):
                return (False)

        if blockList[0].value != None:
            jump = True

        return (True, jump)

    def move(self, jahat, blocks):
        valid = self.moveValid(jahat, blocks)
        if isinstance(valid, bool):
            return False
        if valid[0]:
            jump = valid[1]
            if jahat == 'l':
                if not jump:
                    blocks[self.block.getBlockNumber()].value = None
                    self.block = blocks[self.block.getBlockNumber() - 1]
                    blocks[self.block.getBlockNumber()].value = self
                else:
                    blocks[self.block.getBlockNumber()].value = None
                    self.block = blocks[self.block.getBlockNumber() - 2]
                    blocks[self.block.getBlockNumber()].value = self
            elif jahat == 'r':
                if not jump:
                    blocks[self.block.getBlockNumber()].value = None
                    self.block = blocks[self.block.getBlockNumber() + 1]
                    blocks[self.block.getBlockNumber()].value = self
                else:
                    blocks[self.block.getBlockNumber()].value = None
                    self.block = blocks[self.block.getBlockNumber() + 2]
                    blocks[self.block.getBlockNumber()].value = self
            if jahat == 'u':
                if not jump:
                    blocks[self.block.getBlockNumber()].value = None
                    self.block = blocks[self.block.getBlockNumber() - 9]
                    blocks[self.block.getBlockNumber()].value = self
                else:
                    blocks[self.block.getBlockNumber()].value = None
                    self.block = blocks[self.block.getBlockNumber() - 18]
                    blocks[self.block.getBlockNumber()].value = self
            elif jahat == 'd':
                if not jump:
                    blocks[self.block.getBlockNumber()].value = None
                    self.block = blocks[self.block.getBlockNumber() + 9]
                    blocks[self.block.getBlockNumber()].value = self
                else:
                    blocks[self.block.getBlockNumber()].value = None
                    self.block = blocks[self.block.getBlockNumber() + 18]
                    blocks[self.block.getBlockNumber()].value = self
            return True
        return False
