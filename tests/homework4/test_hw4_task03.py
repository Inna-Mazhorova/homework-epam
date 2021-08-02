import sys

from homework4.hw4_task03 import my_precious_logger


def test_my_precious_logger_error(capsys):
    my_precious_logger("error: file not found")
    captured = capsys.readouterr()
    assert captured.err == "error: file not found"
    assert captured.out == ""


def test_my_precious_logger_no_error_when_ok(capsys):
    my_precious_logger("ok")
    captured = capsys.readouterr()
    assert captured.err == ""
    assert captured.out == "ok"
