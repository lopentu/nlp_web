from html.parser import HTMLParser


class HTMLStripper(HTMLParser):
    """
    The HTMLStripper object strips HTML tags.
    """

    def __init__(self) -> None:
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.fed = []

    def handle_data(self, data) -> None:
        return self.fed.append(data)

    def get_data(self) -> str:
        return "".join(self.fed)

    @classmethod
    def strip_tags(cls, html) -> str:
        html_stripper = cls()
        html_stripper.feed(html)
        return html_stripper.get_data()
