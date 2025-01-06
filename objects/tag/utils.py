from tokens.utils import get_property
from tokens import type


def get_tag(tag_token: dict[str, str]):
    return get_property(tag_token, 'tag_type')


def get_attributes(tag_token: dict[str, str]):
    return get_property(tag_token, 'attributes', {})


def create_empty_object_as(tag: str) -> dict[str, str]:
    return {'type': type.TAG, 'tag': tag, 'attributes': {}, 'children': []}


def create_object_from(token: dict[str, str]):
    return {'type': type.TAG, 'tag': get_tag(token), 'attributes': get_attributes(token), 'children': []}


def add_child_to(object: dict, child: dict[str, str]):
    object['children'].append(child)
