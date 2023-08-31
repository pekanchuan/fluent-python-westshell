import json
from typing import TypedDict


class BookDict(TypedDict):
    isbn: str
    title: str
    authors: list[str]
    pagecount: int


AUTHOR_ELEMENT = '<AUTHOR>{}</AUTHOR>'


def to_xml(book: BookDict) -> str:
    elements: list[str] = []
    for key, value in book.items():
        if isinstance(value, list):
            elements.extend(AUTHOR_ELEMENT.format(n) for n in value)
        else:
            tag = key.upper()
            elements.append(f'<{tag}>{value}</{tag}>')
    xml = '\n\t'.join(elements)
    return f'<BOOK>\n\t{xml}\n</BOOK>'


def from_json(data: str) -> BookDict:
    whatever: BookDict = json.loads(data)
    return whatever


if __name__ == '__main__':
    pp = BookDict(title='Programming Pearls',
                  authors=['Jon Bentley'],
                  isbn='0201657880',
                  pagecount=256)

    print(to_xml(pp))
