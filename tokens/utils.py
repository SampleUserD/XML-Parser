def get_property(token: dict[str, str], prop: str, default=str()):
    return token.get(prop, default)


def get_type(token: dict[str, str]):
    return get_property(token, 'type')