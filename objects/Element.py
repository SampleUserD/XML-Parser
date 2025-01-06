from objects.Node import Node
from objects.Text import Text


class Element(Node):
    __tag__: str = str()
    __attributes__: dict[str, str] = {}
    __parent__: Node = None
    __children__: list[Node] = []

    def __init__(self, tag: str, attributes: dict[str, str] = {}):
        self.__tag__ = tag
        self.__attributes__ = attributes
        self.__children__ = []
        self.__parent__ = None

    def get_by_attribute(self, attr: str, value: str):
        result = []

        for child in self.child_elements:
            if attr in child.attributes:
                result.append(child)
            result.extend(child.get_by_attribute(attr, value))

        return result

    def get_by_tag_name(self, name: str):
        result = []

        for child in self.child_elements:
            if name == child.tag:
                result.append(child)
            result.extend(child.get_by_tag_name(name))

        return result

    def append_child(self, child: Node) -> None:
        self.__children__.append(child)

    def change_contents_to(self, contents: Node) -> Node:
        if isinstance(contents, Element):
            self.__children__ = contents.children
        elif isinstance(contents, Text):
            self.__children__ = [contents]

    @property
    def NODE_TYPE(self):
        return 0

    @property
    def tag(self):
        return self.__tag__

    @property
    def attributes(self):
        return self.__attributes__

    @property
    def parent(self):
        return self.__parent__

    @property
    def children(self):
        return self.__children__

    @property
    def child_elements(self):
        return list(filter(lambda child: isinstance(child, Element), self.children))

    @property
    def text(self):
        return str().join(map(lambda text: text.value, filter(lambda child: isinstance(child, Text), self.children)))

    @property
    def inner_text(self):
        return self.text + str().join(map(lambda element: element.inner_text, self.child_elements))
