from libs.mixins import *
from libs.psychic import *

__all__ = [
    'User',
]


class User(StoreMixin):
    def __init__(self, data):
        super().__init__()
        if data:
            psychic = Psychic(data['psychics'])
            if data['numbers'] is None:
                data['numbers'] = []
            self.data = data
        else:
            psychic = Psychic([])
            self.data = {
                'psychics': psychic.data,
                'numbers': []
            }
        self.psychic = psychic

    def set(self, key, value):
        self.data[key] = value

    def update_index_effectivity(self, number):
        """
        Метод для обновления индекса эффективности экстрасенсов
        :param number: загаданный номер пользователя
        :return:
        """
        for psychic in self.data['psychics']:
            if int(number) == self.data['assessments_map'][psychic['id']]['value']:
                psychic['index_effectivity'] += 1
            else:
                psychic['index_effectivity'] -= 1
