from xmlparser.objects.Node import Node
from xmlparser.objects.Text import Text


class Element(Node):
    __tag__: str = str()
    __attributes__: dict[str, str] = {}
    __parent__: Node = None
    __children__: list[Node] = []

    def __init__(self, tag: str, attributes: dict[str, str] = {}, parent: Node = None):
        self.__tag__ = tag
        self.__attributes__ = attributes
        self.__children__ = []
        self.__parent__ = parent

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

    def insert_after(self, node: Node, after: Node):
        self.__children__.insert(self.__children__.index(after) + 1, node)

    def insert_before(self, node: Node, after: Node):
        self.__children__.insert(self.__children__.index(after) + 1, node)

    def remove(self) -> None:
        if isinstance(self.parent, Element):
            self.parent.__children__.remove(self)

    def change_contents_to(self, contents: Node) -> Node:
        if isinstance(contents, Element):
            self.__children__ = contents.children
        elif isinstance(contents, Text):
            self.__children__ = [contents]

    def to_string(self) -> str:
        string = f'<{self.tag}{' ' if len(self.attributes.keys()) > 0 else ''}{' '.join(map(lambda x: f'{x}="{self.attributes[x]}"', self.attributes))}>'

        for child in self.children:
            if isinstance(child, Element):
                string += child.to_string()
            elif isinstance(child, Text):
                string += f'{child.value}'

        string += f'</{self.tag}>'

        return string

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

    @property
    def inner_xml(self):
        return str().join(map(lambda child: child.to_string(), self.child_elements))

    @property
    def next_sibling(self):
        return self.parent.child_elements[self.parent.child_elements.index(self) + 1]

    @property
    def previous_sibling(self):
        return self.parent.child_elements[self.parent.child_elements.index(self) - 1]
