from xmlparser.objects.Node import Node


class Text(Node):
    __value__: str = str()
    __parent__: Node = None

    def __init__(self, value: str):
       self.__value__ = value

    @property
    def NODE_TYPE(self):
        return 1

    @property
    def value(self):
        return self.__value__

    @property
    def parent(self):
        return self.__parent__


