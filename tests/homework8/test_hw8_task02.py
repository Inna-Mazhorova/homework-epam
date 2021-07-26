import pytest

from homework8.hw8_task02 import TableData


def test_books():
    books = TableData("tests/homework8/example.sqlite", "books")
    assert len(books) == 3
    authors = [item[1] for item in books]
    assert authors == ["Bradbury", "Huxley", "Orwell"]

    # books_list = []
    # for book in books:
    #     books_list.append(books['name'])
    # assert books_list == ["Farenheit 451", "Brave New World", "1984"]


def test_presidents():
    presidents = TableData("tests/homework8/example.sqlite", "presidents")

    with pytest.raises(ValueError, match="There is no line with Putin"):
        presidents["Putin"]

    assert presidents["Yeltsin"] == ("Yeltsin", 999, "Russia")
    assert not "Romanov" in presidents
