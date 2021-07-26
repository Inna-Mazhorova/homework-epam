import sqlite3
from contextlib import contextmanager
from typing import Any, Generator, Optional

"""

Write a wrapper class TableData for database table, that when initialized with database name and table acts as collection object (implements Collection protocol). Assume all data has unique values in 'name' column. So, if presidents = TableData(database_name='example.sqlite', table_name='presidents')

then
len(presidents) will give current amount of rows in presidents table in database
presidents['Yeltsin'] should return single data row for president with name Yeltsin
'Yeltsin' in presidents should return if president with same name exists in table
object implements iteration protocol. i.e. you could use it in for loops::
for president in presidents:
print(president['name'])
all above mentioned calls should reflect most recent data. If data in table changed after you created collection instance, your calls should return updated data.
Avoid reading entire table into memory. When iterating through records, start reading the first record, then go to the next one, until records are exhausted. When writing tests, it's not always neccessary to mock database calls completely. Use supplied example.sqlite file as database fixture file.

"""


class TableData:
    def __init__(self, database: str, chosen_table: str) -> None:
        self.database = database
        self.chosen_table = chosen_table

    @contextmanager
    def connection(self):
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        yield cursor
        cursor.close()
        conn.close()

    def __len__(self) -> int:
        with self.connection() as cursor:
            cursor.execute(f"SELECT COUNT(*) FROM {self.chosen_table}")
            return cursor.fetchone()[0]

    def __getitem__(self, word: str) -> Optional[Any]:
        with self.connection() as cursor:
            cursor.execute(f'SELECT * FROM {self.chosen_table} WHERE name = "{word}"')
            result = cursor.fetchone()
            if result is None:
                raise ValueError(f"There is no line with {word}")
            return result

    def __contains__(self, word: str) -> bool:
        with self.connection() as cursor:
            cursor.execute(f'SELECT * FROM {self.chosen_table} WHERE name = "{word}"')
            return bool(cursor.fetchall())

    def __iter__(self) -> Generator:
        with self.connection() as cursor:
            yield from cursor.execute(f"SELECT * FROM {self.chosen_table}")
