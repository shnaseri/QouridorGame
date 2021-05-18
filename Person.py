from Wall import Wall


class Person:
    persons = []

    def ___init__(self, block, color):
        self.block = block
        self.color = color
        self.wallsRemain = 10

    def AddWall(self, wall):
        if Wall.isValid(self, wall):
            Wall.walls.append(wall)
            self.wallsRemain -= 10
        else:
            return False

    def wallOk(self, jahat, jump):
        if jahat == 'l':
            if Wall.hasWall(Wall(self.x, self.y - 1, 'V')):
                return False
            if jump:
                if Wall.hasWall(Wall(self.x, self.y - 2, 'V')):
                    return False
        elif jahat == 'r':
            if Wall.hasWall(Wall(self.x, self.y, 'V')):
                return False
            if jump:
                if Wall.hasWall(Wall(self.x, self.y + 1, 'V')):
                    return False
        elif jahat == 'u':
            if Wall.hasWall(Wall(self.x - 1, self.y, 'H')):
                return False
            if jump:
                if Wall.hasWall(Wall(self.x - 2, self.y, 'H')):
                    return False
        elif jahat == 'd':
            if Wall.hasWall(Wall(self.x, self.y, 'H')):
                return False
            if jump:
                if Wall.hasWall(Wall(self.x + 9, self.y, 'H')):
                    return False
        return True

    def moveValid(self, jahat, blocks):
        blockList = self.block.getBlocks()
        jump = False
        if len(blockList) == 0:
            return (False)
        if len(blockList == 1):
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
        if valid[0]:
            jump = valid[1]
            if jahat == 'l':
                if not jump:
                    self.block.y -= 1
                    blocks[self.block.getBlockNumber()].value = None
                    blocks[self.block.getBlockNumber() - 1].value = self.color
                else:
                    self.block.y -= 2
                    blocks[self.block.getBlockNumber()].value = None
                    blocks[self.block.getBlockNumber() - 2].value = self.color
            elif jahat == 'r':
                if not jump:
                    self.block.y += 1
                    blocks[self.block.getBlockNumber()].value = None
                    blocks[self.block.getBlockNumber() + 1].value = self.color
                else:
                    self.block.y += 2
                    blocks[self.block.getBlockNumber()].value = None
                    blocks[self.block.getBlockNumber() + 2].value = self.color
            if jahat == 'u':
                if not jump:
                    self.block.x -= 1
                    blocks[self.block.getBlockNumber()].value = None
                    blocks[self.block.getBlockNumber() - 9].value = self.color
                else:
                    self.block.x -= 2
                    blocks[self.block.getBlockNumber()].value = None
                    blocks[self.block.getBlockNumber() - 18].value = self.color
            elif jahat == 'd':
                if not jump:
                    self.block.x += 1
                    blocks[self.block.getBlockNumber()].value = None
                    blocks[self.block.getBlockNumber() + 9].value = self.color
                else:
                    self.block.x += 2
                    blocks[self.block.getBlockNumber()].value = None
                    blocks[self.block.getBlockNumber() + 18].value = self.color
            return True
        return False
