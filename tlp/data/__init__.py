from .utils import *
from .mtg import open_mtg
from .shakespeare import open_tiny_shakespeare
from enum import Enum


class DataLoader(Enum):
    mtg = open_mtg
    tiny_shakespeare = open_tiny_shakespeare

    def __call__(self, *args):
        self.value(*args)
