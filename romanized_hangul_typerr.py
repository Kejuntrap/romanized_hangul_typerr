import io, sys
import jk_converter as jk

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

hangul_vowel = [
    "ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅗ", "ㅘ", "ㅙ", "ㅚ", "ㅛ", "ㅜ", "ㅝ", "ㅞ", "ㅟ", "ㅠ", "ㅡ", "ㅢ", "ㅣ"
]

vowel_rr = ["a", "ae", "ya", "yae", "eo", "e", "yeo", "ye", "o", "wa", "wae", "oe", "yo", "u", "wo", "we", "wi", "yu",
            "eu", "ui", "i"]

consonant_rr = ["g", "kk", "n", "d", "tt", "r", "m", "b", "pp", "s", "ss", "", "j", "jj", "ch", "k", "t", "p", "h"]
hangul_consonant = [
    "ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"
]

batchim_wov_rr = ["", "k", "k", "kt", "n", "nt", "nh", "t", "l", "lk", "lm", "lp", "lt", "lt", "lp", "lh", "m", "p",
                  "pt", "t", "t", "ng", "t", "t", "k", "t", "p", "h"]
batchim_wv_rr = ["", "g", "kk", "ks", "n", "nj", "nh", "d", "r", "lg", "lm", "lb", "ls", "lt", "lp", "lh", "m", "b",
                 "ps", "s", "ss", "ng", "j", "ch", "k", "t", "p", "h"]
hangul_batchim = [
    [""], ["ᆨ", "ᄀ"], ["ᆩ", "ᄁ"], ["ᆪ"], ["ᆫ", "ᄂ"], ["ᆬ", "ᅜ"], ["ᆭ", "ᅝ"], ["ᆮ", "ᄃ"], ["ᆯ", "ᄅ"], ["ᆰ"], ["ᆱ"],
    ["ᆲ"], ["ᆳ"],
    ["ᆴ"], ["ᆵ"], ["ᆶ", "ᄚ"], ["ᆷ", "ᄆ"], ["ᆸ", "ᄇ"], ["ᆹ", "ᄡ"], ["ᆺ", "ᄉ"], ["ᆻ", "ᄊ"], ["ᆼ", "ᄋ"], ["ᆽ", "ᄌ"],
    ["ᆾ", "ᄎ"],
    ["ᆿ", "ᄏ"], ["ᇀ", "ᄐ"], ["ᇁ", "ᄑ"], ["ᇂ", "ᄒ"]
]

# keyは　ハングルのアルファベット表記＋日本語入力＋ハングル
duplication_memorize = {}  # 同じハングルと読みが登録されていないか?

delim = "\t"
nl = "\n"
w_type = "固有名詞"


def main():
    output_tsv()
    print(len(duplication_memorize))


def hangul_unicode(_c, _v, _b):
    return 0xAC00 + _c * 0x24C + _v * 0x1C + _b


def hangul_pronounce(code, _next_vowel):
    code -= 0xAC00
    _c = code // 0x24C
    _v = (code - _c * 0x24C) // 0x1C
    _b = code % 0x1C
    if _next_vowel:
        return consonant_rr[_c] + vowel_rr[_v] + batchim_wv_rr[_b]
    else:
        return consonant_rr[_c] + vowel_rr[_v] + batchim_wov_rr[_b]


def get_key(_pronounce, _chr):
    if type(_chr) == int:
        return _pronounce + jk.romaji_to_jp_input(_pronounce) + str(chr(_chr))
    if type(_chr) == str:
        return _pronounce + jk.romaji_to_jp_input(_pronounce) + _chr


def output_tsv():   # １文字のハングルや子音，母音，パッチムの予測変換を作る
    f = open("romanized_hangul_typerr.txt", "w", encoding="utf-16le")
    f.write('\ufeff')
    for vi in range(0, len(vowel_rr)):
        for ci in range(0, len(consonant_rr)):
            for bi in range(0, len(batchim_wv_rr)):
                h_uni = hangul_unicode(ci, vi, bi)
                hp1 = hangul_pronounce(h_uni, False)
                hp2 = hangul_pronounce(h_uni, True)

                if get_key(hp1, h_uni) not in duplication_memorize:
                    _str = jk.romaji_to_jp_input(hp1) + delim + str(chr(h_uni)) + delim + w_type + nl
                    duplication_memorize[get_key(hp1, h_uni)] = 1

                if jk.romaji_to_jp_input(hp1)[-1] == "ｎ" and hp1 + jk.romaji_to_jp_input(hp1).replace("ｎ", "ん") + str(
                        chr(h_uni)) not in duplication_memorize:
                    _str += jk.romaji_to_jp_input(hp1).replace("ｎ", "ん") + delim + str(
                        chr(h_uni)) + delim + w_type + nl  # ぱｎ(판)のように最後がｎで終わるやつがんに変換されても出るようにする
                    duplication_memorize[hp1 + jk.romaji_to_jp_input(hp1).replace("ｎ", "ん") + str(chr(h_uni))] = 1

                if hp1 != hp2 and get_key(hp2, h_uni) not in duplication_memorize:  # 後にくるハングルで読みが変わるやつはそれも登録する
                    _str += jk.romaji_to_jp_input(hp2) + delim + str(chr(h_uni)) + delim + w_type + nl
                    duplication_memorize[get_key(hp2, h_uni)] = 1
                    if jk.romaji_to_jp_input(hp2)[-1] == "ｎ" and hp2 + jk.romaji_to_jp_input(hp2).replace("ｎ", "ん") + str(
                            chr(h_uni)) not in duplication_memorize:
                        _str += jk.romaji_to_jp_input(hp2).replace("ｎ", "ん") + delim + str(
                            chr(h_uni)) + delim + w_type + nl  # ぱｎ(판)のように最後がｎで終わるやつがんに変換されても出るようにする
                        duplication_memorize[hp2 + jk.romaji_to_jp_input(hp2).replace("ｎ", "ん") + str(chr(h_uni))] = 1

                if len(_str) > 0:
                    f.write(_str)

    # 母音ㅏやㅗなど ㅇをngと母音で出せるようにする ㅇㅈをいｊで出せるようにする
    for i in range(0, len(hangul_vowel)):
        if get_key(vowel_rr[i], hangul_vowel[i]) not in duplication_memorize:
            f.write(jk.romaji_to_jp_input(vowel_rr[i]) + delim + hangul_vowel[i] + delim + w_type + nl)
            duplication_memorize[get_key(vowel_rr[i], hangul_vowel[i])] = 1

        if get_key(vowel_rr[i], "ㅇ") not in duplication_memorize:
            f.write(jk.romaji_to_jp_input(vowel_rr[i]) + delim + "ㅇ" + delim + w_type + nl)
            duplication_memorize[get_key(vowel_rr[i], "ㅇ")] = 1

        f.write("んｇ" + delim + "ㅇ" + delim + w_type + nl)  # ㅇㅈ インジョンを いｊで出せるようにする
        duplication_memorize["ngんｇㅇ"] = 1

    # 子音
    for i in range(0, len(hangul_consonant)):
        if len(jk.romaji_to_jp_input(consonant_rr[i])) > 0 and get_key(consonant_rr[i], hangul_consonant[i]) not in duplication_memorize:  # 無音のㅇを登録するのはあまりよろしくない
            f.write(jk.romaji_to_jp_input(consonant_rr[i]) + delim + hangul_consonant[i] + delim + w_type + nl)
            duplication_memorize[get_key(consonant_rr[i], hangul_consonant[i])] = 1

    # パッチム
    for i in range(1, len(hangul_batchim)):  # 0はパッチムがつかないハングル用なので
        for j in range(0, len(hangul_batchim[i])):
            if get_key(batchim_wov_rr[i], hangul_batchim[i][j]) not in duplication_memorize:
                f.write(jk.romaji_to_jp_input(batchim_wov_rr[i]) + delim + hangul_batchim[i][j] + delim + w_type + nl)
                duplication_memorize[get_key(batchim_wov_rr[i], hangul_batchim[i][j])] = 1

            if get_key(batchim_wv_rr[i], hangul_batchim[i][j]) not in duplication_memorize:
                f.write(jk.romaji_to_jp_input(batchim_wv_rr[i]) + delim + hangul_batchim[i][j] + delim + w_type + nl)
                duplication_memorize[get_key(batchim_wv_rr[i], hangul_batchim[i][j])] = 1

    f.close()


if __name__ == '__main__':
    main()
