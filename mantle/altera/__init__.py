import os

target = os.getenv('MANTLE_TARGET', 'cyclone4')

assert target == 'cyclone4'

from .mantle4 import *

print('import mantle cyclone4')



