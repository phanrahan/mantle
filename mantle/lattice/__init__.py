import os

target = os.environ.get('MANTLE_TARGET', 'ice40')

assert target == 'ice40'

from .mantle40 import *


