import sys

from homework4.hw4_task03 import my_precious_logger


def test_my_precious_logger_error(capsys):
    my_precious_logger("error: file not found")
    captured = capsys.readouterr()
    assert captured.err == "error: file not found"


def test_my_precious_logger_error_no_out(capsys):
    my_precious_logger("error: file not found")
    out, err = capsys.readouterr()
    sys.stdout.write(out)
    sys.stderr.write(err)
    assert out == ""


def test_my_precious_logger_no_error_when_ok(capsys):
    my_precious_logger("ok")
    captured = capsys.readouterr()
    assert captured.err == ""


def test_my_precious_logger_not_error(capsys):
    my_precious_logger("ok")
    out, err = capsys.readouterr()
    sys.stdout.write(out)
    sys.stderr.write(err)
    assert out == "ok"
