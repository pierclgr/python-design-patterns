# BUILDER PATTER
# The builder pattern solve the problem that sometimes the creation of an object
# requires a lot of operations and/or parameters and thus, calling the constructor
# straightforwardly is not a good idea. The builder pattern creates an object Builder
# that is used to build the object step by step. The builder aims at separating the
# object building logic from the representation
from typing import List


class HTMLElement:
    def __init__(self, name: str = "", content: str = "") -> None:
        self.name: str = name
        self.content: str = content
        self.child_elements: List[HTMLElement] = []
        self.__n_indent_chars: int = 2
        self.__indent_character: str = " "

    def add_child(self, child: "HTMLElement") -> None:
        self.child_elements.append(child)

    def clear_children(self):
        self.child_elements.clear()

    def __str__(self) -> str:
        return self.__str()

    def __str(self, indent_level: int = 0) -> str:
        output_string = ""
        n_indent_chars = (indent_level * self.__n_indent_chars)
        if len(self.child_elements) > 0:
            content = "\n" + "\n".join(
                [child_element.__str(indent_level + 1) for child_element in
                 self.child_elements]) + "\n"
            closing_tag = f"{n_indent_chars * self.__indent_character}</{self.name}>"
        else:
            content = self.content
            closing_tag = f"</{self.name}>"

        opening_tag = f"{n_indent_chars * self.__indent_character}<{self.name}>"
        output_string += f"{opening_tag}{content}{closing_tag}"

        return output_string

    @staticmethod
    def create(name: str = "") -> "HTMLBuilder":
        return HTMLBuilder(root_element=name)


class HTMLBuilder:
    def __init__(self, root_element: HTMLElement | str = None):
        if not root_element:
            root_element = HTMLElement("html")
        elif isinstance(root_element, str):
            root_element = HTMLElement(root_element)
        self.__root_element: HTMLElement = root_element

    def add_child(self, name: str, content: str = "") -> "HTMLBuilder":
        child_element = HTMLElement(name, content)
        self.__root_element.add_child(child_element)
        return HTMLBuilder(child_element)

    def clear_children(self):
        self.__root_element.clear_children()

    def __str__(self):
        return str(self.__root_element)


html = HTMLElement.create()
html.add_child("header")
list = html.add_child("body").add_child("div").add_child("li")
list.add_child("ul", "prova1")
list.add_child("ul", "prova1")
list.add_child("ul", "prova1")
html.add_child("footer")
print(html)
