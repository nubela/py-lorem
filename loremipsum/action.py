import os
from random import choice

__author__ = 'nubela'
__here__ = os.path.dirname(os.path.abspath(__file__))
__lorem_file__ = os.path.join(__here__, "loremipsum.txt")


def sentence(max_char=None):
    """
    Gets a random sentence from a lorem ipsum paragraph.
    """
    para_text = paragraph()
    sent = filter(lambda x: x != "", para_text.split("."))
    s = choice(sent)
    return __strip(s[:max_char]) + "."


def paragraph(max_char=None):
    """
    Gets a random paragraph from a lorem ipsum prose.
    """
    para_text = choice(__paragraphs())
    return __strip(para_text[:max_char])


def __paragraphs():
    """
    Get a list of paragraphs from the lorem file
    """
    f = open(__lorem_file__, 'r')
    return filter(lambda x: x != "", f.readlines())


def __strip(str):
    """
    Removes extra whitespace
    """
    return ' '.join(str.split())