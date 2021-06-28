from typing import List


def get_rarest_char(file_path: str) -> List[str]:
    with open(file_path, "r") as infile:
        words = infile.read().split()
        words_clean = list(
            map(lambda x: x.encode("ascii").decode("unicode_escape"), words)
        )
        text_clean = " ".join(words_clean)
    elements = {}
    for i in text_clean:
        if i not in elements:
            elements[i] = 1
        else:
            elements[i] += 1
    minimum_list = []
    for i in elements:
        if elements[i] == 1:
            minimum_list.append(i)
    return minimum_list
