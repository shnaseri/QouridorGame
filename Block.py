class Block:
    blocks = []
    x = -1
    y = -1
    value = None

    def getBlockNumber(self):
        return (9 * self.x) + self.y

    def __init__(self, x, y, person=None):
        self.x = x
        self.y = y
        self.value = person

    def getBlocks(self, jahat):
        blockList = []
        if jahat == 'l':
            if self.y >= 1:
                blockList.append(Block.blocks[self.getBlockNumber() - 1])
            if self.y > 1:
                blockList.append(Block.blocks[self.getBlockNumber() - 2])
        elif jahat == 'r':
            if self.y <= 8:
                blockList.append(Block.blocks[self.getBlockNumber() + 1])
            if self.y < 8:
                blockList.append(Block.blocks[self.getBlockNumber() + 2])
        elif jahat == 'u':
            if self.x >= 1:
                blockList.append(Block.blocks[self.getBlockNumber() - 9])
            if self.x > 1:
                blockList.append(Block.blocks[self.getBlockNumber() - 18])
        elif jahat == 'd':
            if self.x <= 8:
                blockList.append(Block.blocks[self.getBlockNumber() + 9])
            if self.x < 8:
                blockList.append(Block.blocks[self.getBlockNumber() + 18])
        return blockList
