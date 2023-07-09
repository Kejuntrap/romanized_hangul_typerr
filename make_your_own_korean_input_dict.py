import sys

import base as b

default_input_file = "korean_words.txt"


def make_your_own_korean_input_dict():
    file = None
    if len(sys.argv) == 1:
        file = open(default_input_file, 'r', encoding="utf-8")
    else:
        file = open(sys.argv[1], 'r', encoding="utf-8")

    f = b.DictionaryWriter()
    f.init("output.txt", b.FILE_ENCODING)

    for a in file.readlines():
        a_content = (a.replace(b.NL, "")).split(",")
        if len(a_content[0]) > 0 and a_content[0][0] != b.COMMENT:
            if len(a_content) == 1:
                f.wl([b.dictionary_word_maker(a_content[0]), a_content[0], b.W_TYPE], b.DELIM)
            else:
                f.wl([b.dictionary_word_maker(a_content[0]), a_content[0], a_content[1]], b.DELIM)
    f.close()


if __name__ == '__main__':
    make_your_own_korean_input_dict()
