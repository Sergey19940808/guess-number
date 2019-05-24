from django.core.cache import cache

from libs.mixins import *

__all__ = [
    'Store'
]


class Store(StoreMixin):
    def __init__(self):
        super().__init__()
        self.data = cache
