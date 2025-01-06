from objects import *

from re import match


def output(tree, offset=0):
    print(f'{'\t'*offset}\\{tree.tag}')

    for child in tree.children:
        if isinstance(child, XMLElement):
            output(child, offset + 1)
        else:
            if match('\\S', child.value):
                print(f'{'\t'*offset}\t\\"{child.value}"')