from enum import Enum
from enum import IntEnum
from enum import auto


class Move(IntEnum):
    UP = 1
    DOWN = auto()
    LEFT = 5
    RIGHT = auto()


print(Move["UP"])
for x in Move:
    print(x.value)
