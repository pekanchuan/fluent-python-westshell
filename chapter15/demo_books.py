from books import BookDict
from typing import TYPE_CHECKING


def demo() -> None:
    book = BookDict(
        title='Programming Pearls',
        authors=['Jon Bentley'],
        isbn='0201657880',
        pagecount=256
    )
    authors = book['authors']
    if TYPE_CHECKING:
        reveal_type(authors)
    authors = 'Bob'
    book['weight'] = 4.2
    del book['title']


if __name__ == '__main__':
    demo()
