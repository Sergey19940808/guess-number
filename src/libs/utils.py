from uuid import getnode as get_mac
from random import randint

__all__ = [
    'build_context',
    'assessmented_psychics',
    'get_macaddress',
    'update_assumptions',
]

USER = {
    'psychics': [
        {'id': 0, 'name': 'Vlad', 'assumptions': [], 'index_effectivity': 0},
        {'id': 1, 'name': 'Genady', 'assumptions': [], 'index_effectivity': 0},
        {'id': 2, 'name': 'Petr', 'assumptions': [], 'index_effectivity': 0}
    ],
    'numbers': [

    ],

}


def _create_or_get_user(store):
    """
    Метод для создания и/или получения экстрасенсов
    :param store: объект для работы с хранилищем данных
    :return:
    """
    mac = get_macaddress()
    if store.get(mac):
        return store.get(mac)
    else:
        store.set(mac, USER)
        return store.get(mac)


def build_context(store):
    """
    Метод для формирования контекста
    :param store: объект для работы с хранилищем данных
    :return:
    """
    user = _create_or_get_user(store)
    return user


def assessmented_psychics(psychics, number):
    """
    Метод для формирования оценки экстрасенсов
    :param psychics: список экстрасенсов
    :param number: введенное число пользователем
    :return:
    """
    assessments = {
        psychic['id']: {'value': randint(int(number) - 5, int(number) + 5), 'name': psychic['name']}
        for psychic in psychics
    }
    return assessments


def get_macaddress():
    return get_mac()


def update_assumptions(psychics, assessments):
    for psychic in psychics:
        psychic['assumptions'].append(assessments.get(psychic['id'])['value'])
    return psychics

