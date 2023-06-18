import io, sys
import jk_converter as jk
import romanized_hangul_typerr as rh

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
#sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# 現在の入力法では　seokyeol（석열）を連続して打てないのでそれの改善を行う

rensetsu = {}

def main():
    """
    for vi in range(0, len(rh.vowel_rr)):
        for ci in range(0, len(rh.consonant_rr)):
            for bi in range(0, len(rh.batchim_wv_rr)):
                h_uni = rh.hangul_unicode(ci, vi, bi)

    print(jk.rji_debug("seokyeol")) # seokyeo l
    print(jk.extract_vowel("seokyeo"))  # seok yeo

    print(jk.rji_debug("seok")) # seo k
    print(jk.extract_vowel("seo"))  # s eo


    print(jk.rji_debug("eopseo"))  # eopseo *
    print(jk.extract_vowel("eopseo"))  # eops eo
    print(jk.rji_debug("eops"))  # eo ps
    print(jk.extract_vowel("eo"))  # * eo
"""
    for vi in range(0, len(rh.vowel_rr)):
        for ci in range(0, len(rh.consonant_rr)):   # 11
            for bi in range(0, len(rh.batchim_wv_rr)):
                h_uni = rh.hangul_unicode(ci, vi, bi)

                for vii in range(0, len(rh.vowel_rr)):
                    for bii in range(0, len(rh.batchim_wv_rr)):
                        h_uni_2 = rh.hangul_unicode(11, vii, bii)
                        rensetsu[str(chr(h_uni))+str(chr(h_uni_2))] = 0
    print(len(rensetsu))

if __name__ == '__main__':
    main()


# seokyeol seo kyeo l
# eops eo    eo pseo

