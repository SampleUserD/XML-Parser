from xmlparser.objects.Element import Element
from xmlparser.objects.Text import Text

from re import match


def output(tree, offset=0):
    print(f'{'\t'*offset}<{tree.tag}{' ' if len(tree.attributes.keys()) > 0 else ''}{' '.join(map(lambda x: f'{x}="{tree.attributes[x]}"', tree.attributes))}>')

    for child in tree.children:
        if isinstance(child, Element):
            output(child, offset + 1)
        elif isinstance(child, Text):
            if child.value.strip() != str():
                print(f'{'\t'*offset}\t"{child.value.strip()}"')

    print(f'{'\t' * offset}</{tree.tag}>')