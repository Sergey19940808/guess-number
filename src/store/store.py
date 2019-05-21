from django.core.cache import cache

__all__ = [
    'Store'
]


class Store(object):
    def set(self, key, value):
        cache.set(key, value)

    def get(self, key):
        return cache.get(key)