from xmlparser.objects.Element import Element
from xmlparser.objects.Text import Text

from re import match


def output(tree, offset=0):
    print(f'{'\t'*offset}\\<{tree.tag}>')

    for child in tree.children:
        if isinstance(child, Element):
            output(child, offset + 1)
        elif isinstance(child, Text):
            if match('\\S', child.value):
                print(f'{'\t'*offset}\t\\"{child.value}"')