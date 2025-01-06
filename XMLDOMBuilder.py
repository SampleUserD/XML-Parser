from tokens.comps import is_tag, is_text, is_closing_tag
from tokens.text import get_value
from tokens.tag import get_tag, get_attributes
from objects import *

from typing import Callable


class XMLDOMBuilder:
    __counter__ = 0
    __tokens__ = []

    def __init__(self, tokens: list[dict[str, str]]):
        self.__tokens__ = tokens

    # -------------------------------------------------------------#

    def __current__(self) -> dict[str, str]:
        return self.__tokens__[self.__counter__] if self.__counter__ < len(self.__tokens__) else {}

    def __peek__(self) -> dict[str, str]:
        self.__counter__ += 1
        return self.__current__()

    # -------------------------------------------------------------#

    def __with__(self, work: Callable):
        result = work(self.__current__())
        self.__peek__()
        return result

    # -------------------------------------------------------------#

    @property
    def __done__(self):
        return self.__counter__ >= len(self.__tokens__)

    # -------------------------------------------------------------#

    def __add_elements_to_until__(self, element: XMLElement, condition: Callable):
        while not condition():
            current_token = self.__current__()
            if is_tag(current_token):
                element.append_child(self.__build_tree__(element))
            elif is_text(current_token):
                element.append_child(XMLText(get_value(current_token), element))
            else:
                raise Exception()

            self.__peek__()

    def __build_tree__(self, parent):
        tag = self.__current__()
        element = self.__with__(lambda ct: XMLElement(get_tag(ct), get_attributes(ct), parent))

        self.__add_elements_to_until__(
            element,
            lambda:
                get_tag(tag) == get_tag(self.__current__()) \
                and is_closing_tag(self.__current__()))

        return element

    # -------------------------------------------------------------#

    def build(self):
        document = XMLElement('Document')

        self.__add_elements_to_until__(document, lambda: self.__done__)

        return document

