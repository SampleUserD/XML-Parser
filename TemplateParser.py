def __are_tokens_equal__(token_1: dict, token_2: dict):
    return token_1.get('type', str()) == token_2.get('type', str()) \
        and token_1.get('value', str()) == token_2.get('value', str())


class TemplateParser:
    __tokens__ = []
    __counter__ = 0

    def __init__(self, tokens: list):
        self.__tokens__ = tokens

    # -------------------------------------------------------------#

    def __current__(self) -> dict[str, str]:
        return self.__tokens__[self.__counter__] if self.__counter__ < len(self.__tokens__) else {}

    def __next__(self) -> dict[str, str]:
        self.__counter__ += 1
        return self.__current__()

    def __lookup__(self, offset: int) -> dict:
        return self.__tokens__[self.__counter__ + offset] \
            if self.__counter__ + offset < len(self.__tokens__) else {}

    def __match__(self, tokens: list) -> bool:
        index = 0

        while len(tokens) > index and __are_tokens_equal__(self.__lookup__(index), tokens[index]):
            index += 1

        return index == len(tokens)

    # -------------------------------------------------------------#

    # -------------------------------------------------------------#

    def parse(self):
        print('')
        pass
