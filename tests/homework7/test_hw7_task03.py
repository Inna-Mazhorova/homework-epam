import pytest

from homework7.hw7_task03 import tic_tac_toe_checker

board_o_wins = [["-", "x", "-"], ["o", "o", "o"], ["-", "x", "x"]]

board_x_wins = [["o", "x", "-"], ["o", "-", "o"], ["x", "x", "x"]]

board_draw = [["x", "x", "o"], ["o", "o", "x"], ["x", "x", "o"]]

board_error_both = [["o", "x", "o"], ["o", "o", "o"], ["x", "x", "x"]]

board_incorrect_amount = [["-", "-", "o"], ["-", "o", "o"], ["x", "x", "x"]]

board_not_finished = [["x", "-", "o"], ["o", "o", "x"], ["x", "x", "o"]]

board_wrong_symbol = [["x", "P", "o"], ["o", "o", "x"], ["x", "x", "o"]]


def test_x_wins():
    assert tic_tac_toe_checker(board_x_wins) == "x wins!"


def test_o_wins():
    assert tic_tac_toe_checker(board_o_wins) == "o wins!"


def test_draw():
    assert tic_tac_toe_checker(board_draw) == "draw!"


def test_not_finished():
    assert tic_tac_toe_checker(board_not_finished) == "unfinished"


def test_error_win_both():
    with pytest.raises(ValueError, match="X and O can't win both!"):
        tic_tac_toe_checker(board_error_both)


def test_error_incorrect_amount():
    with pytest.raises(ValueError, match="Incorrect amount of x and o!"):
        tic_tac_toe_checker(board_incorrect_amount)


def test_error_wrong_symbol():
    with pytest.raises(ValueError, match="You entered wrong symbol"):
        tic_tac_toe_checker(board_wrong_symbol)
