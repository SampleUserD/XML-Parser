from tokens.comps import is_tag, is_closing_tag
from tokens import type

from tokens.tag import *


class XMLCorrecter:
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

    def __lookup__(self, offset: int) -> dict[str, str]:
        return self.__tokens__[self.__counter__ + offset] \
            if self.__counter__ + offset < len(self.__tokens__) \
            else create_empty_object_as('__global__')

    # -------------------------------------------------------------#

    def __is_closing_tag_exists__(self):
        index = 1
        token = self.__current__()

        while (get_tag(token) != get_tag(self.__lookup__(index))
                or not is_closing_tag(self.__lookup__(index))) \
                and self.__counter__ + index < len(self.__tokens__):
            index += 1

        return self.__counter__ + index != len(self.__tokens__)

    # -------------------------------------------------------------#

    def correct(self):
        while self.__counter__ < len(self.__tokens__):
            if is_tag(self.__current__()) and not self.__is_closing_tag_exists__():
                self.__tokens__.insert(self.__counter__ + 1, { 'type': type.CLOSING_TAG, 'attributes': [], 'tag_type': get_tag(self.__current__())})

            self.__peek__()

        return self.__tokens__
