import base as b


def romaji_to_jp_input(_str):  # パッチム付きのハングルをパッチムの領域とそうでない領域に分ける
    split = 0
    ret = ""
    d = False
    for i in range(0, len(_str)):
        for j in range(0, len(b.VOWELS)):
            if _str[-i - 1] == b.VOWELS[j] and not d:
                split = len(_str) - i
                d = True
                break
    if 0 < split:
        ret += b.RR_TO_JP[_str[0:split]]
    if split < len(_str):
        ret += b.RR_TO_JP[_str[split:len(_str)]]
    return ret


def rji_debug(_str):
    split = 0
    ret = ""
    d = False
    for i in range(0, len(_str)):
        for j in range(0, len(b.VOWELS)):
            if _str[-i - 1] == b.VOWELS[j] and not d:
                split = len(_str) - i
                d = True
                break
    print(0, split, split, len(_str))


def extract_vowel(_str):  # パッチムの無い領域において後ろから最長の母音列を取り出す
    split = 0
    d = False
    if len(_str) >= 3:
        for vl in range(0, 3):
            for i in range(0, len(b.VOWEL_VOLUME[vl])):
                if _str[-3 + vl:] == b.VOWEL_VOLUME[vl][i] and not d:  # マッチするものが見つかったら
                    split = len(_str) - 3 + vl
                    d = True
                    break
    else:
        for vl in range(3 - len(_str), 3):
            for i in range(0, len(b.VOWEL_VOLUME[vl])):
                if _str[-len(_str) + vl:] == b.VOWEL_VOLUME[vl][i] and not d:  # マッチするものが見つかったら
                    split = len(_str) - len(_str) + vl
                    d = True
                    break
    print(0, split, split, len(_str))
