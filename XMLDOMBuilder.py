from tokens.comps import is_tag, is_text, is_closing_tag
from tokens.text import get_value
from tokens.tag import get_tag, get_attributes
from objects import *


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

    @property
    def __done__(self):
        return self.__counter__ >= len(self.__tokens__)

    # -------------------------------------------------------------#

    def __build_tree__(self, parent):
        if not is_tag(self.__current__()):
            return XMLElement('__global__')

        token = self.__current__()
        element = XMLElement(get_tag(token), get_attributes(token), parent)
        self.__peek__()

        while get_tag(token) != get_tag(self.__current__()) or not is_closing_tag(self.__current__()):
            if is_tag(self.__current__()):
                element.append_child(self.__build_tree__(element))
            elif is_text(self.__current__()):
                element.append_child(XMLText(get_value(self.__current__()), element))
            else:
                raise Exception()

            self.__peek__()

        return element

    # -------------------------------------------------------------#

    def build(self):
        document = XMLElement('Document')

        while not is_tag(self.__current__()) and not self.__done__:
            if is_text(self.__current__()):
                document.append_child(XMLText(get_value(self.__current__()), document))
            else:
                raise Exception()
            self.__peek__()

        while not self.__done__:
            current_token = self.__current__()
            if is_tag(current_token):
                document.append_child(self.__build_tree__(document))
            elif is_text(current_token):
                document.append_child(XMLText(get_value(current_token), document))
            else:
                raise Exception()
            self.__peek__()

        return document

