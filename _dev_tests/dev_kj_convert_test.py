import base as b
import time as t
sum_of_hangeul_pairs = 11172 * 11172     # 124,813,584


def kj():       # ハングルのローマ字転写から日本語入力変換のテスト　cover率100%になったのでOK
    s_time = t.time()
    for vi1 in range(0, len(b.VOWEL_RR)):
        for ci1 in range(0, len(b.CONSONANT_RR)):
            for bi1 in range(0, len(b.BATCHIM_WV_RR)):
                h_uni1 = b.hangul_unicode(ci1, vi1, bi1)
                for vi2 in range(0, len(b.VOWEL_RR)):
                    for ci2 in range(0, len(b.CONSONANT_RR)):
                        for bi2 in range(0, len(b.BATCHIM_WV_RR)):
                            h_uni2 = b.hangul_unicode(ci2, vi2, bi2)
                            b.convert_romaji_jp_type(b.hangul_pronounce(h_uni1, False) + b.hangul_pronounce(h_uni2, False))
                            b.convert_romaji_jp_type(b.hangul_pronounce(h_uni1, True) + b.hangul_pronounce(h_uni2, False))
    print((t.time() - s_time)*1000, "ms")


if __name__ == '__main__':
    kj()
