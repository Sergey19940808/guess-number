from random import randint
from uuid import getnode as get_mac
from django.views.generic import View

from libs.store import *
from libs.user import *

__all__ = [
    'BaseView',
]


class BaseView(View):
    template_name = 'guess_number/main.html'
    store = Store()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user = self.build_context(self.store)
        self.mac = self.get_macaddress()

    def _create_or_get_user(self, store):
        """
        Метод для создания и/или получения пользователя
        :param store: объект для работы с хранилищем данных
        :return:
        """
        mac = self.get_macaddress()
        if store.data.get(mac):
            user = User(store.data.get(mac))
            return user
        else:
            user = User([])
            store.data.set(mac, user.data)
            return user

    def build_context(self, store):
        """
        Метод для формирования контекста
        :param store: объект для работы с хранилищем данных
        :return:
        """
        user = self._create_or_get_user(store)
        return user

    @staticmethod
    def get_macaddress():
        """
        Метод для получения мак адреса
        :return:
        """
        return get_mac()

    @staticmethod
    def assessmented_psychics(psychics, number):
        """
        Метод для формирования оценки экстрасенсов
        :param psychics: список экстрасенсов
        :param number: введенное число пользователем
        :return:
        """
        assessments = {
            psychic['id']: {
                'id': psychic['id'],
                'value': randint(int(number) - 3, int(number) + 3),
                'name': psychic['name']
            }
            for psychic in psychics
        }
        return assessments

    def sync_store(self):
        self.store.set(self.mac, self.user.get_data())
