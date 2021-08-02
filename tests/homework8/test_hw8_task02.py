import pytest

from homework8.hw8_task02 import TableData


def test_books():
    books = TableData(database="tests/homework8/example.sqlite", chosen_table="books")
    assert len(books) == 3
    authors = [item[1] for item in books]
    assert authors == ["Bradbury", "Huxley", "Orwell"]

    books_list = []
    for book in books:
        books_list.append(book["name"])
    assert books_list == ["Farenheit 451", "Brave New World", "1984"]


def test_presidents():
    presidents = TableData(
        database="tests/homework8/example.sqlite", chosen_table="presidents"
    )

    with pytest.raises(ValueError, match="There is no line with Putin"):
        presidents["Putin"]

    assert tuple(presidents["Yeltsin"]) == ("Yeltsin", 999, "Russia")
    assert not "Romanov" in presidents
