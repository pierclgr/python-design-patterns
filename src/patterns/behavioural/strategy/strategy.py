# Strategy Pattern
# The strategy pattern is used to decompose an algorithm into a high level and a low level part. This way,
# we can have a high level general part while the low level can be adapted for different needs or vice versa.
from abc import ABC
from enum import Enum, auto


# low-level part of the algorithm
class ListStrategy(ABC):
    def start(self, buffer): pass

    def end(self, buffer): pass

    def add_list_item(self, buffer, item): pass


class MarkdownListStrategy(ListStrategy):
    def add_list_item(self, buffer, item):
        buffer.append(f" * {item}")


class HTMLListStrategy(ListStrategy):
    def start(self, buffer):
        buffer.append(f"<ul>\n")

    def end(self, buffer):
        buffer.append("</ul>\n")

    def add_list_item(self, buffer, item):
        buffer.append(f"\t<li>{item}</li>\n")


class OutputFormat(Enum):
    MARKDOWN = auto()
    HTML = auto()


# high-level part of the algorithm
class TextProcessor:
    def __init__(self, list_strategy=HTMLListStrategy()):
        self.buffer = []
        self.list_strategy = list_strategy

    def append_list(self, items):
        ls = self.list_strategy
        ls.start(self.buffer)
        for item in items:
            ls.add_list_item(self.buffer, item)
        ls.end(self.buffer)

    def set_output_format(self, format):
        if format == OutputFormat.MARKDOWN:
            self.list_strategy = MarkdownListStrategy()
        elif format == OutputFormat.HTML:
            self.list_strategy = HTMLListStrategy()

    def clear(self):
        self.buffer.clear()

    def __str__(self):
        return "".join(self.buffer)


if __name__ == "__main__":
    item = ["foo", "bar", "baz"]

    tp = TextProcessor()
    tp.set_output_format(OutputFormat.MARKDOWN)
    tp.append_list(item)
    print(tp)

    tp.set_output_format(OutputFormat.HTML)
    tp.clear()
    tp.append_list(item)
    print(tp)
