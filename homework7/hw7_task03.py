from collections import Counter
from typing import List

import numpy as np

"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"
Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"
    [[-, -, o],
     [-, o, o],
     [x, x, x]]
     Return value should be "x wins!"
"""


def tic_tac_toe_checker(board: List[List]) -> str:
    numpy_board = np.array(board)
    first_row = numpy_board[0]
    second_row = numpy_board[1]
    third_row = numpy_board[2]
    first_column = numpy_board.T[0]
    second_column = numpy_board.T[1]
    third_column = numpy_board.T[2]
    diagonal_1 = np.diagonal(numpy_board)
    diagonal_2 = np.diagonal(np.fliplr(numpy_board))
    variants_list = [
        first_row,
        second_row,
        third_row,
        first_column,
        second_column,
        third_column,
        diagonal_1,
        diagonal_2,
    ]
    amount_elements = Counter(first_row) + Counter(second_row) + Counter(third_row)
    resuls_list_x = list(
        map(lambda z: z == 3, map(sum, map(lambda y: y == ["x"], variants_list)))
    )
    resuls_list_0 = list(
        map(lambda z: z == 3, map(sum, map(lambda y: y == ["o"], variants_list)))
    )
    if amount_elements["x"] + amount_elements["o"] + amount_elements["-"] != 9:
        raise ValueError("You entered wrong symbol")
    if any(resuls_list_x) and any(resuls_list_0):
        raise ValueError("X and O can't win both!")
    if any(resuls_list_x) and amount_elements["x"] == (amount_elements["o"] + 1):
        return "x wins!"
    if any(resuls_list_0) and amount_elements["x"] == amount_elements["o"]:
        return "o wins!"
    if not amount_elements["-"] and amount_elements["x"] == (amount_elements["o"] + 1):
        return "draw!"
    if (
        (
            amount_elements["x"] == (amount_elements["o"] + 1)
            or amount_elements["x"] == amount_elements["o"]
        )
        and not any(resuls_list_0)
        and not any(resuls_list_x)
    ):
        return "unfinished"
    raise ValueError("Incorrect amount of x and o!")
