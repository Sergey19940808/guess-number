from django.views.generic import View

from libs.store import Store
from libs.utils import (
    build_context,
    get_macaddress,
)


__all__ = [
    'BaseView',
]


class BaseView(View):
    template_name = 'guess_number/main.html'
    store = Store()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = build_context(self.store)
        self.mac = get_macaddress()
        self.user = self.store.get(self.mac)