from homework2.hw2_task01_part1 import get_longest_diverse_words


def test_get_longest_diverse_words():
    assert get_longest_diverse_words("tests/homework2/data.txt") == [
        "unmißverständliche",
        "Bevölkerungsabschub",
        "Kollektivschuldiger",
        "Werkstättenlandschaft",
        "Schicksalsfiguren",
        "Selbstverständlich",
        "Fingerabdrucks",
        "Friedensabstimmung",
        "außenpolitisch",
        "Seinsverdichtungen",
    ]
