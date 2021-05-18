class Wall:
    walls = []

    def __init__(self, x, y, o) -> None:
        self.startX = x
        self.startY = y
        self.orientation = o

    @staticmethod
    def hasWall(wall):
        if wall.orientation == 'H':
            if wall.startX in [i.x for i in Wall.walls] or wall.startX + 1 in [i.x for i in Wall.walls]:
                return True
        else:
            if wall.startY in [i.y for i in Wall.walls] or wall.startY + 1 in [i.y for i in Wall.walls]:
                return True
        return False

    def isValid(person, wall):
        if Wall.hasWall(wall):
            return False
        elif person.wallsRemain < 1:
            return False
        elif wall.orientation == 'H' and wall.startX > (n - 1):
            return False
        elif wall.orientation == 'V' and wall.startY > (n - 1):
            return False
        elif wall.startY < 0 or wall.startX < 0:
            return False
        else:
            return True
