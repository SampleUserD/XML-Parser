from re import match
from tokens import type


class XMLTokenizer:
    __counter__ = 0
    __tokens__ = []
    __string__ = str()

    def __init__(self, string):
        self.__string__ = string
        self.__tokens__ = []

    # -------------------------------------------------------------#

    def __current__(self) -> str:
        return self.__string__[self.__counter__] if self.__counter__ < len(self.__string__) else str()

    def __peek__(self) -> str:
        self.__counter__ += 1
        return self.__current__()

    def __lookup__(self, offset: int) -> str:
        return self.__string__[self.__counter__ + offset] \
            if self.__counter__ + offset < len(self.__string__) \
            else str()

    def __match__(self, substring: str) -> bool:
        index = 0

        while len(substring) > index and self.__lookup__(index) == substring[index]:
            index += 1

        return index == len(substring)

    def __skip_all_of__(self, character: str) -> None:
        while self.__current__() == character:
            self.__peek__()

    def __skip_length_of__(self, substring: str) -> None:
        for index in range(len(substring)):
            self.__peek__()

    # -------------------------------------------------------------#

    def __extract_text__(self, opening: str, ending: str) -> str:
        text = str()

        if self.__match__(opening):
            self.__skip_length_of__(opening)
            while not self.__match__(ending):
                text += self.__current__()
                self.__peek__()
            self.__skip_length_of__(ending)

        return text

    def __extract_block__(self, opening: str, ending: str) -> str:
        block = str()
        level = 0

        if self.__match__(opening):
            self.__skip_length_of__(opening)
            while (not self.__match__(ending) and level == 0) or (level > 0):
                if self.__match__(opening): level += 1
                if self.__match__(ending): level -= 1

                block += self.__current__()
                self.__peek__()
            self.__skip_length_of__(ending)

        return block

    # -------------------------------------------------------------#

    def __add_token__(self, token: dict[str, str]) -> None:
        self.__tokens__.append(token)

    # -------------------------------------------------------------#

    def __tokenize_tag__(self) -> None:
        if not self.__match__('<'): return None
        value = self.__extract_text__('<', '>').strip().split(' ', 1)

        tag = value[0]
        attributes = {}

        ending_index = 0

        attribute_regexp = '\\s*([a-zA-Z0-9_\\-\\+\\@\\$\\[\\]\\.]+)\\s*=\\s*\"(.*?)\"'

        while len(value) == 2 and match(attribute_regexp, value[1][ending_index::]):
            result = match(attribute_regexp, value[1][ending_index::])
            attributes[result.group(1)] = result.group(2)
            ending_index += result.span()[1]

        _type = type.OPENING_TAG if tag[0] != '/' else type.CLOSING_TAG
        _tag_type =  tag if tag[0] != '/' else tag[1::]

        self.__add_token__({'type': _type, 'tag_type': _tag_type, 'attributes': attributes})

    def __tokenize_template(self) -> None:
        if not self.__match__('{'): return None
        value = self.__extract_block__('{', '}')

        self.__add_token__({'type': 'TEMPLATE', 'value': value})

    def __tokenize_comment__(self) -> None:
        comment = self.__extract_text__('<!--', '-->')

    def __tokenize_text__(self) -> None:
        text = str()

        while match('[^<>]', self.__current__()):
            text += self.__current__()
            self.__peek__()

        if text != str():
            self.__add_token__({'type': type.TEXT, 'value': text})

    def tokenize(self) -> list:
        while self.__counter__ < len(self.__string__):
            self.__tokenize_comment__()
            self.__tokenize_tag__()
            self.__tokenize_template()
            self.__tokenize_text__()

        return self.__tokens__
