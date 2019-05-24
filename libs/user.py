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
            self.data = data
        else:
            psychic = Psychic([])
            self.data = {
                'psychics': psychic.data,
                'numbers': []
            }
        self.psychic = psychic

    def update_index_effectivity(self):
        """
        Метод для обновления индекса эффективности экстрасенсов
        :return:
        """
        for psychic in self.psychic.data:
            if int(self.data['number']) == self.data['assessments_map'][psychic['id']]['value']:
                psychic['index_effectivity'] += 1
            else:
                psychic['index_effectivity'] -= 1
