from xmlparser.tokens.utils import get_property


def get_value(text_token: dict[str, str]):
    return get_property(text_token, 'value')
