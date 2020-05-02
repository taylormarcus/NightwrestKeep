class _Actor:
    def __init__(self):
        self._isdead = False

    @property
    def isdead(self):
        return self.isdead

    @isdead.setter
    def isdead(self, value):
        if isinstance(value, bool):
            self._isdead = value


class _Player(_Actor):
    def __init__(self):
        super().__init__()
        self._locale = None
        self._items = []

    @property
    def item(self):
        return self._items

    @item.setter
    def item(self, item):
        if item not in self._items:
            self._items.append(item)

    @property
    def locale(self):
        return self._locale

    @locale.setter
    def locale(self, locale):
        self._locale = locale
