from xmlparser.objects.Node import Node


class Text(Node):
    __value__: str = str()
    __parent__: Node = None

    def __init__(self, value: str, parent: Node = None):
        self.__value__ = value
        self.__parent__ = parent

    @property
    def NODE_TYPE(self):
        return 1

    @property
    def value(self):
        return self.__value__

    @property
    def parent(self):
        return self.__parent__


