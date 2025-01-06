from tokens.comps import is_tag, is_text
from objects.tag.utils import *
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

    def __build_tree__(self, parent):
        if not is_tag(self.__current__()):
            return XMLElement('__global__')

        token = self.__current__()
        element = XMLElement(get_tag(token), get_attributes(token))
        element.__parent__ = parent
        self.__peek__()

        while get_tag(token) != get_tag(self.__current__()):
            if is_tag(self.__current__()):
                element.append_child(self.__build_tree__(element))
            elif is_text(self.__current__()):
                text = XMLText(self.__current__()['value'])
                text.__parent__ = element
                element.append_child(text)
            else:
                raise Exception()

            self.__peek__()

        return element

    # -------------------------------------------------------------#

    def build(self):
        __global__ = XMLElement('__global__')

        while not is_tag(self.__current__()) and len(self.__tokens__) > self.__counter__:
            if is_text(self.__current__()):
                text = XMLText(self.__current__()['value'])
                text.__parent__ = __global__
                __global__.append_child(text)
            else:
                raise Exception()
            self.__peek__()

        while self.__counter__ < len(self.__tokens__):
            if is_tag(self.__current__()):
                __global__.append_child(self.__build_tree__(__global__))
            elif is_text(self.__current__()):
                text = XMLText(self.__current__()['value'])
                text.__parent__ = __global__
                __global__.append_child(text)
            else:
                raise Exception()
            self.__peek__()

        return __global__
