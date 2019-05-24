from libs.mixins import *

__all__ = [
    'Psychic',
]


class Psychic(StoreMixin):
    def __init__(self, data):
        super().__init__()
        if data:
            self.data = data
        else:
            self.data = [
                {'id': 0, 'name': 'Vlad', 'assumptions': [], 'index_effectivity': 0},
                {'id': 1, 'name': 'Genady', 'assumptions': [], 'index_effectivity': 0},
                {'id': 2, 'name': 'Petr', 'assumptions': [], 'index_effectivity': 0}
            ]

    def set(self, key, value):
        self.data[key] = value

    def update_assumptions(self, assessments):
        """
        Метод для обновления догадок экстрасенсов
        :param assessments: список словарей догадок
        :return:
        """
        for psychic in self.data:
            psychic['assumptions'].append(assessments.get(psychic['id'])['value'])
        return self.data
