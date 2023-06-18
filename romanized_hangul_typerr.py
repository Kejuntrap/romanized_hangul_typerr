import io, sys
import jk_converter as jk
import base as b

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# keyは　ハングルのアルファベット表記＋日本語入力＋ハングル
duplication_memorize = {}  # 同じハングルと読みが登録されていないか?


def main():
    output_tsv()
    print("done")
    # print(len(duplication_memorize))


def hangul_unicode(_c, _v, _b):
    return 0xAC00 + _c * 0x24C + _v * 0x1C + _b


def hangul_pronounce(code, _next_vowel):
    code -= 0xAC00
    _c = code // 0x24C
    _v = (code - _c * 0x24C) // 0x1C
    _b = code % 0x1C
    if _next_vowel:
        return b.CONSONANT_RR[_c] + b.VOWEL_RR[_v] + b.BATCHIM_WV_RR[_b]
    else:
        return b.CONSONANT_RR[_c] + b.VOWEL_RR[_v] + b.BATCHIM_WOV_RR[_b]


def get_key(_pronounce, _chr):
    if type(_chr) == int:
        return _pronounce + jk.romaji_to_jp_input(_pronounce) + str(chr(_chr))
    if type(_chr) == str:
        return _pronounce + jk.romaji_to_jp_input(_pronounce) + _chr


def output_tsv():  # １文字のハングルや子音，母音，パッチムの予測変換を作る
    f = open("romanized_hangul_typerr.txt", "w", encoding="utf-16le")
    f.write('\ufeff')
    for vi in range(0, len(b.VOWEL_RR)):
        for ci in range(0, len(b.CONSONANT_RR)):
            for bi in range(0, len(b.BATCHIM_WV_RR)):
                h_uni = hangul_unicode(ci, vi, bi)
                hp1 = hangul_pronounce(h_uni, False)
                hp2 = hangul_pronounce(h_uni, True)

                if get_key(hp1, h_uni) not in duplication_memorize:
                    _str = jk.romaji_to_jp_input(hp1) + b.DELIM + str(chr(h_uni)) + b.DELIM + b.W_TYPE + b.NL
                    duplication_memorize[get_key(hp1, h_uni)] = 1

                if jk.romaji_to_jp_input(hp1)[-1] == "ｎ" and hp1 + jk.romaji_to_jp_input(hp1).replace("ｎ", "ん") + str(
                        chr(h_uni)) not in duplication_memorize:
                    _str += jk.romaji_to_jp_input(hp1).replace("ｎ", "ん") + b.DELIM + str(
                        chr(h_uni)) + b.DELIM + b.W_TYPE + b.NL  # ぱｎ(판)のように最後がｎで終わるやつがんに変換されても出るようにする
                    duplication_memorize[hp1 + jk.romaji_to_jp_input(hp1).replace("ｎ", "ん") + str(chr(h_uni))] = 1

                if hp1 != hp2 and get_key(hp2, h_uni) not in duplication_memorize:  # 後にくるハングルで読みが変わるやつはそれも登録する
                    _str += jk.romaji_to_jp_input(hp2) + b.DELIM + str(chr(h_uni)) + b.DELIM + b.W_TYPE + b.NL
                    duplication_memorize[get_key(hp2, h_uni)] = 1
                    if jk.romaji_to_jp_input(hp2)[-1] == "ｎ" and hp2 + jk.romaji_to_jp_input(hp2).replace("ｎ", "ん") + str(
                            chr(h_uni)) not in duplication_memorize:
                        _str += jk.romaji_to_jp_input(hp2).replace("ｎ", "ん") + b.DELIM + str(
                            chr(h_uni)) + b.DELIM + b.W_TYPE + b.NL  # ぱｎ(판)のように最後がｎで終わるやつがんに変換されても出るようにする
                        duplication_memorize[hp2 + jk.romaji_to_jp_input(hp2).replace("ｎ", "ん") + str(chr(h_uni))] = 1

                if len(_str) > 0:
                    f.write(_str)

    # 母音ㅏやㅗなど ㅇをngと母音で出せるようにする ㅇㅈをいｊで出せるようにする
    for i in range(0, len(b.HANGEUL_VOWEL)):
        if get_key(b.VOWEL_RR[i], b.HANGEUL_VOWEL[i]) not in duplication_memorize:
            f.write(jk.romaji_to_jp_input(b.VOWEL_RR[i]) + b.DELIM + b.HANGEUL_VOWEL[i] + b.DELIM + b.W_TYPE + b.NL)
            duplication_memorize[get_key(b.VOWEL_RR[i], b.HANGEUL_VOWEL[i])] = 1

        if get_key(b.VOWEL_RR[i], "ㅇ") not in duplication_memorize:
            f.write(jk.romaji_to_jp_input(b.VOWEL_RR[i]) + b.DELIM + "ㅇ" + b.DELIM + b.W_TYPE + b.NL)
            duplication_memorize[get_key(b.VOWEL_RR[i], "ㅇ")] = 1

        f.write("んｇ" + b.DELIM + "ㅇ" + b.DELIM + b.W_TYPE + b.NL)  # ㅇㅈ インジョンを いｊで出せるようにする
        duplication_memorize["ngんｇㅇ"] = 1

    # 子音
    for i in range(0, len(b.HANGEUL_CONSONANT)):
        if len(jk.romaji_to_jp_input(b.CONSONANT_RR[i])) > 0 and get_key(b.CONSONANT_RR[i],
                                                                         b.HANGEUL_CONSONANT[i]) not in duplication_memorize:  # 無音のㅇを登録するのはあまりよろしくない
            f.write(jk.romaji_to_jp_input(b.CONSONANT_RR[i]) + b.DELIM + b.HANGEUL_CONSONANT[i] + b.DELIM + b.W_TYPE + b.NL)
            duplication_memorize[get_key(b.CONSONANT_RR[i], b.HANGEUL_CONSONANT[i])] = 1

    # パッチム
    for i in range(1, len(b.HANGEUL_BATCHIM)):  # 0はパッチムがつかないハングル用なので
        for j in range(0, len(b.HANGEUL_BATCHIM[i])):
            if get_key(b.BATCHIM_WOV_RR[i], b.HANGEUL_BATCHIM[i][j]) not in duplication_memorize:
                f.write(jk.romaji_to_jp_input(b.BATCHIM_WOV_RR[i]) + b.DELIM + b.HANGEUL_BATCHIM[i][j] + b.DELIM + b.W_TYPE + b.NL)
                duplication_memorize[get_key(b.BATCHIM_WOV_RR[i], b.HANGEUL_BATCHIM[i][j])] = 1

            if get_key(b.BATCHIM_WV_RR[i], b.HANGEUL_BATCHIM[i][j]) not in duplication_memorize:
                f.write(jk.romaji_to_jp_input(b.BATCHIM_WV_RR[i]) + b.DELIM + b.HANGEUL_BATCHIM[i][j] + b.DELIM + b.W_TYPE + b.NL)
                duplication_memorize[get_key(b.BATCHIM_WV_RR[i], b.HANGEUL_BATCHIM[i][j])] = 1

    f.close()


if __name__ == '__main__':
    main()
