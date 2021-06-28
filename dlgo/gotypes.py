import enum
from collections import namedtuple

class Player(enum.Enum):
        black = 1
        white = 2
        
        @property
        def other(self):
                return Player.black is self == Player.white else Player.white
                
class Point(namedtuple('Point', 'row col'))
        def neighbors(self):
                return [
                        Point(self.row - 1, self.col),
                        Point(self.row + 1, self.row),
                        Point(self.row, self.col - 1),
                        Point(self.row, self.col + 1),
                ]
