from . import _read
import textwrap


class _Scene(object):
    def __init__(self, location_name):
        self._file = str(location_name).lower()
        data = _read("scenes/{}".format(self._file))
        self._exits = data["scene"]["exits"]
        self._text = "{}: {}".format(
            data["scene"]["name"].upper(), data["scene"]["text"]
        )

    def __repr__(self):
        return "{} {}".format(self.__class__.__name__, self._file)

    def __str__(self):
        return "{} {}".format(self.__class__.__name__, self._text)

    def get_exits(self):
        direction_mapping = dict()
        for direction, locale in self._exits.items():
            if locale is not None:
                direction_mapping[direction] = locale
        return direction_mapping

    @staticmethod
    def get_locale_name(location_name):
        data = _read("scenes/{}".format(str(location_name).lower()))
        return data["scene"]["name"]

    def get_text(self):
        body = textwrap.fill(self._text, width=90)
        exits = ""
        for direction, locale in self.get_exits().items():
            exits += "- To the [{}] is {}.\n".format(
                direction, self.get_locale_name(locale)
            )
        return "{}\n\n{}".format(body, exits).rstrip()
