from XMLTokenizer import XMLTokenizer
from XMLCorrecter import XMLCorrecter
from XMLDOMBuilder import XMLDOMBuilder


def parse(xml: str):
    return XMLDOMBuilder(XMLCorrecter(XMLTokenizer(xml).tokenize()).correct()).build()