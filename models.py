from collections import namedtuple
from enum import Enum

Point = namedtuple('Point', ['x', 'y'])
Size = namedtuple('Size', ['width', 'height'])


class Direction(Enum):
    LEFT = 'l'
    RIGHT = 'r'
    UP = 'u'
    DOWN = 'd'
