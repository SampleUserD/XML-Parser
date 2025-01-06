from tokens import type
from tokens.utils import get_type


def is_tag(token: dict[str, str]):
    return get_type(token) == type.TAG


def is_opening_tag(token: dict[str, str]):
    return get_type(token) == type.OPENING_TAG


def is_closing_tag(token: dict[str, str]):
    return get_type(token) == type.CLOSING_TAG


def is_text(token: dict[str, str]):
    return get_type(token) == type.TEXT
