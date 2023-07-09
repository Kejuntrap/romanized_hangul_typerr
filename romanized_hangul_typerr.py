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


def get_key(_pronounce, _chr):  # ダブりを確認するための辞書配列のキーを作る関数
    if type(_chr) == int:
        return _pronounce + jk.romaji_to_jp_input(_pronounce) + str(chr(_chr))
    if type(_chr) == str:
        return _pronounce + jk.romaji_to_jp_input(_pronounce) + _chr


def output_tsv():  # １文字のハングルや子音，母音，パッチムの予測変換を作る
    f: b.DictionaryWriter = b.DictionaryWriter()
    f.init("romanized_hangul_typerr.txt", b.FILE_ENCODING)
    for vi in range(0, len(b.VOWEL_RR)):
        for ci in range(0, len(b.CONSONANT_RR)):
            for bi in range(0, len(b.BATCHIM_WV_RR)):
                h_uni = b.hangul_unicode(ci, vi, bi)
                hp1 = b.hangul_pronounce(h_uni, False)
                hp2 = b.hangul_pronounce(h_uni, True)

                if get_key(hp1, h_uni) not in duplication_memorize:
                    f.wl([jk.romaji_to_jp_input(hp1), str(chr(h_uni)), b.W_TYPE], b.DELIM)
                    duplication_memorize[get_key(hp1, h_uni)] = 1

                if jk.romaji_to_jp_input(hp1)[-1] == "ｎ" and hp1 + jk.romaji_to_jp_input(hp1).replace("ｎ", "ん") + str(chr(h_uni)) not in duplication_memorize:
                    f.wl([jk.romaji_to_jp_input(hp1).replace("ｎ", "ん"), str(chr(h_uni)), b.W_TYPE], b.DELIM)  # ぱｎ(판)のように最後がｎで終わるやつがんに変換されても出るようにする
                    duplication_memorize[hp1 + jk.romaji_to_jp_input(hp1).replace("ｎ", "ん") + str(chr(h_uni))] = 1

                if hp1 != hp2 and get_key(hp2, h_uni) not in duplication_memorize:  # 後にくるハングルで読みが変わるやつはそれも登録する
                    f.wl([jk.romaji_to_jp_input(hp2), str(chr(h_uni)), b.W_TYPE], b.DELIM)
                    duplication_memorize[get_key(hp2, h_uni)] = 1
                    if jk.romaji_to_jp_input(hp2)[-1] == "ｎ" and hp2 + jk.romaji_to_jp_input(hp2).replace("ｎ", "ん") + str(
                            chr(h_uni)) not in duplication_memorize:
                        f.wl([jk.romaji_to_jp_input(hp2).replace("ｎ", "ん"), str(chr(h_uni)), b.W_TYPE], b.DELIM)  # ぱｎ(판)のように最後がｎで終わるやつがんに変換されても出るようにする
                        duplication_memorize[hp2 + jk.romaji_to_jp_input(hp2).replace("ｎ", "ん") + str(chr(h_uni))] = 1

    # 母音ㅏやㅗなど ㅇをngと母音で出せるようにする ㅇㅈをいｊで出せるようにする
    for i in range(0, len(b.HANGEUL_VOWEL)):
        if get_key(b.VOWEL_RR[i], b.HANGEUL_VOWEL[i]) not in duplication_memorize:
            f.wl([jk.romaji_to_jp_input(b.VOWEL_RR[i]), b.HANGEUL_VOWEL[i], b.W_TYPE], b.DELIM)
            duplication_memorize[get_key(b.VOWEL_RR[i], b.HANGEUL_VOWEL[i])] = 1

        if get_key(b.VOWEL_RR[i], "ㅇ") not in duplication_memorize:
            f.wl([jk.romaji_to_jp_input(b.VOWEL_RR[i]), "ㅇ", b.W_TYPE], b.DELIM)
            duplication_memorize[get_key(b.VOWEL_RR[i], "ㅇ")] = 1

        f.wl(["んｇ", "ㅇ", b.W_TYPE], b.DELIM)
        duplication_memorize["ngんｇㅇ"] = 1

    # 子音
    for i in range(0, len(b.HANGEUL_CONSONANT)):
        if len(jk.romaji_to_jp_input(b.CONSONANT_RR[i])) > 0 and get_key(b.CONSONANT_RR[i],
                                                                         b.HANGEUL_CONSONANT[i]) not in duplication_memorize:  # 無音のㅇを登録するのはあまりよろしくない
            f.wl([jk.romaji_to_jp_input(b.CONSONANT_RR[i]), b.HANGEUL_CONSONANT[i], b.W_TYPE], b.DELIM)
            duplication_memorize[get_key(b.CONSONANT_RR[i], b.HANGEUL_CONSONANT[i])] = 1

    # パッチム
    for i in range(1, len(b.HANGEUL_BATCHIM)):  # 0はパッチムがつかないハングル用なので
        for j in range(0, len(b.HANGEUL_BATCHIM[i])):
            if get_key(b.BATCHIM_WOV_RR[i], b.HANGEUL_BATCHIM[i][j]) not in duplication_memorize:
                f.wl([jk.romaji_to_jp_input(b.BATCHIM_WOV_RR[i]), b.HANGEUL_BATCHIM[i][j], b.W_TYPE], b.DELIM)
                duplication_memorize[get_key(b.BATCHIM_WOV_RR[i], b.HANGEUL_BATCHIM[i][j])] = 1

            if get_key(b.BATCHIM_WV_RR[i], b.HANGEUL_BATCHIM[i][j]) not in duplication_memorize:
                f.wl([jk.romaji_to_jp_input(b.BATCHIM_WV_RR[i]), b.HANGEUL_BATCHIM[i][j], b.W_TYPE], b.DELIM)
                duplication_memorize[get_key(b.BATCHIM_WV_RR[i], b.HANGEUL_BATCHIM[i][j])] = 1

    f.close()


if __name__ == '__main__':
    main()
