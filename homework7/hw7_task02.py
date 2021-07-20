"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".
    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".
    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".
"""


def word_without_backspace(word: str):
    if "#" not in word:
        return word

    i = 0
    new_word = ""
    while i < len(word):
        if word[i] == "#" and new_word:
            new_word = new_word[:-1]
        elif word[i] != "#":
            new_word += word[i]
        i += 1
    return new_word


def backspace_compare(first: str, second: str):
    return word_without_backspace(first) == word_without_backspace(second)
