from xmlparser.tokens.utils import get_property
from xmlparser.tokens.type import *

def get_tag(tag_token: dict[str, str]):
    return get_property(tag_token, 'tag_type')


def get_attributes(tag_token: dict[str, str]):
    return get_property(tag_token, 'attributes')


def get_attributes(tag_token: dict[str, str]):
    return get_property(tag_token, 'attributes')


def create_empty_object_as(tag: str):
    return {'type': TAG, 'tag_type': tag, 'attributes': {}}