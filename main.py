from XMLParse import parse

from objects import *

from utils.XMLOutput import output

from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Приложение на Tkinter')
root.geometry('300x500')

# Продумать API для работы с XML-деревом

code = '''
Hello world!
Hello world 2!
<Button x="100">
    <!--
    <Text>Hello world!</Text>
    -->
    <Text>
        <Text>Hello!</Text>
    </Text>
</Button>
'''
DOM = parse(code)


def handle_button(node: XMLElement):
    attrs = node.attributes
    button = Button(text=node.get_by_tag_name('Text')[0].inner_text)

    button.pack(anchor="nw",
                padx=float(attrs.get('x', 0)),
                pady=float(attrs.get('y', 0)))


def handle_title(node: XMLElement):
    root.title(node.inner_text)


def handle_text(node: XMLText):
    print(node.value)
    label = Label(text=node.value)
    label.pack(anchor="nw")


register = { 'Button': handle_button, 'Title': handle_title }

output(DOM)

for node in DOM.children:
    if isinstance(node, XMLText):
        handle_text(node)
    if isinstance(node, XMLElement):
        register[node.tag](node)

root.mainloop()
