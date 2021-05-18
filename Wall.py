class Wall:
    walls = []
    def __init__(self, x, y, o) -> None:
        self.startX = x
        self.startY = y
        self.orientation = o
    
    @classmethod
    def hasWall(wall):
        if wall.orientation == 'H':
            if wall.x in [i.x for i in Wall.walls] or wall.x + 1 in [i.x for i in Wall.walls]:
                return True
        else:
            if wall.y in [i.y for i in Wall.walls] or wall.y + 1 in [i.y for i in Wall.walls]:
                return True
        return False

    def isValid(person, wall):
        if Wall.hasWall(wall):
            return False
        else:
            return True