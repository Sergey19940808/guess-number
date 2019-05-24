__all__ = [
    'StoreMixin',
]


class StoreMixin(object):
    def __init__(self):
        self.data = None

    def get(self, key):
        return self.data.get(key)

    def remove(self, key):
        self.data.pop(key)

    def set(self, key, value):
        self.data.set(key, value)

    def get_data(self):
        return self.data
