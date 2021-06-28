def get_most_common_non_ascii_char(file_path: str) -> str:
    with open(file_path, "r") as infile:
        words = infile.read().split()
        words_clean = list(
            map(lambda x: x.encode("ascii").decode("unicode_escape"), words)
        )
        text_clean = " ".join(words_clean)
    non_ascii_text = "".join(filter(lambda x: ord(x) > 127, text_clean))
    non_ascii_elements = {}
    for i in non_ascii_text:
        if i not in non_ascii_elements:
            non_ascii_elements[i] = 1
        else:
            non_ascii_elements[i] += 1
    maximum = max(non_ascii_elements, key=lambda x: non_ascii_elements[x])
    return maximum
