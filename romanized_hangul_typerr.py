vowel_rr = ["a", "ae", "ya", "yae", "eo", "e", "yeo", "ye", "o", "wa", "wae", "oe", "yo", "u", "wo", "we", "wi", "yu",
            "eu", "ui", "i"]
consonant_rr = ["g", "kk", "n", "d", "tt", "r", "m", "b", "pp", "s", "ss", "", "j", "jj", "ch", "k", "t", "p", "h"]
batchim_wov_rr = ["", "k", "k", "kt", "n", "nt", "nh", "t", "l", "lk", "lm", "lp", "lt", "lt", "lp", "lh", "m", "p",
                  "pt", "t", "t", "ng", "t", "t", "k", "t", "p", "h"]
batchim_wv_rr = ["", "g", "kk", "ks", "n", "nj", "nh", "d", "r", "lg", "lm", "lb", "ls", "lt", "lp", "lh", "m", "b",
                 "ps", "s", "ss", "ng", "j", "ch", "k", "t", "p", "h"]

rr_to_jp = {
    "a": "あ", "eo": "えお", "o": "お", "u": "う", "eu": "えう", "i": "い", "ae": "あえ", "e": "え",
    "oe": "おえ", "wi": "うぃ", "ya": "や", "yeo": "いぇお", "yo": "よ", "yu": "ゆ", "yae": "やえ",
    "ye": "いぇ", "wa": "わ", "wae": "わえ", "wo": "を", "we": "うぇ", "ui": "うい", "ga": "が",
    "geo": "げお", "go": "ご", "gu": "ぐ", "geu": "げう", "gi": "ぎ", "gae": "がえ", "ge": "げ",
    "goe": "ごえ", "gwi": "ぐぃ", "gya": "ぎゃ", "gyeo": "ぎぇお", "gyo": "ぎょ", "gyu": "ぎゅ",
    "gyae": "ぎゃえ", "gye": "ぎぇ", "gwa": "ぐぁ", "gwae": "ぐぁえ", "gwo": "ぐぉ", "gwe": "ぐぇ",
    "gui": "ぐい", "ka": "か", "keo": "けお", "ko": "こ", "ku": "く", "keu": "けう", "ki": "き",
    "kae": "かえ", "ke": "け", "koe": "こえ", "kwi": "ｋうぃ", "kya": "きゃ", "kyeo": "きぇお",
    "kyo": "きょ", "kyu": "きゅ", "kyae": "きゃえ", "kye": "きぇ", "kwa": "くぁ", "kwae": "くぁえ",
    "kwo": "ｋを", "kwe": "ｋうぇ", "kui": "くい", "kka": "っか", "kkeo": "っけお", "kko": "っこ",
    "kku": "っく", "kkeu": "っけう", "kki": "っき", "kkae": "っかえ", "kke": "っけ", "kkoe": "っこえ",
    "kkwi": "ｋｋうぃ", "kkya": "っきゃ", "kkyeo": "っきぇお", "kkyo": "っきょ", "kkyu": "っきゅ",
    "kkyae": "っきゃえ", "kkye": "っきぇ", "kkwa": "っくぁ", "kkwae": "っくぁえ", "kkwo": "ｋｋを",
    "kkwe": "ｋｋうぇ", "kkui": "っくい", "da": "だ", "deo": "でお", "do": "ど", "du": "づ",
    "deu": "でう", "di": "ぢ", "dae": "だえ", "de": "で", "doe": "どえ", "dwi": "どぃ", "dya": "ぢゃ",
    "dyeo": "ぢぇお", "dyo": "ぢょ", "dyu": "ぢゅ", "dyae": "ぢゃえ", "dye": "ぢぇ", "dwa": "どぁ",
    "dwae": "どぁえ", "dwo": "どぉ", "dwe": "どぇ", "dui": "づい", "ta": "た", "teo": "てお",
    "to": "と", "tu": "つ", "teu": "てう", "ti": "ち", "tae": "たえ", "te": "て", "toe": "とえ",
    "twi": "とぃ", "tya": "ちゃ", "tyeo": "ちぇお", "tyo": "ちょ", "tyu": "ちゅ", "tyae": "ちゃえ",
    "tye": "ちぇ", "twa": "とぁ", "twae": "とぁえ", "two": "とぉ", "twe": "とぇ", "tui": "つい",
    "tta": "った", "tteo": "ってお", "tto": "っと", "ttu": "っつ", "tteu": "ってう", "tti": "っち",
    "ttae": "ったえ", "tte": "って", "ttoe": "っとえ", "ttwi": "っとぃ", "ttya": "っちゃ",
    "ttyeo": "っちぇお", "ttyo": "っちょ", "ttyu": "っちゅ", "ttyae": "っちゃえ", "ttye": "っちぇ",
    "ttwa": "っとぁ", "ttwae": "っとぁえ", "ttwo": "っとぉ", "ttwe": "っとぇ", "ttui": "っつい",
    "ba": "ば", "beo": "べお", "bo": "ぼ", "bu": "ぶ", "beu": "べう", "bi": "び", "bae": "ばえ",
    "be": "べ", "boe": "ぼえ", "bwi": "ｂうぃ", "bya": "びゃ", "byeo": "びぇお", "byo": "びょ",
    "byu": "びゅ", "byae": "びゃえ", "bye": "びぇ", "bwa": "ｂわ", "bwae": "ｂわえ", "bwo": "ｂを",
    "bwe": "ｂうぇ", "bui": "ぶい", "pa": "ぱ", "peo": "ぺお", "po": "ぽ", "pu": "ぷ", "peu": "ぺう",
    "pi": "ぴ", "pae": "ぱえ", "pe": "ぺ", "poe": "ぽえ", "pwi": "ｐうぃ", "pya": "ぴゃ",
    "pyeo": "ぴぇお", "pyo": "ぴょ", "pyu": "ぴゅ", "pyae": "ぴゃえ", "pye": "ぴぇ", "pwa": "ｐわ",
    "pwae": "ｐわえ", "pwo": "ｐを", "pwe": "ｐうぇ", "pui": "ぷい", "ja": "じゃ", "jeo": "じぇお",
    "jo": "じょ", "ju": "じゅ", "jeu": "じぇう", "ji": "じ", "jae": "じゃえ", "je": "じぇ",
    "joe": "じょえ", "jwi": "ｊうぃ", "jya": "じゃ", "jyeo": "じぇお", "jyo": "じょ", "jyu": "じゅ",
    "jyae": "じゃえ", "jye": "じぇ", "jwa": "ｊわ", "jwae": "ｊわえ", "jwo": "ｊを", "jwe": "ｊうぇ",
    "jui": "じゅい", "jja": "っじゃ", "jjeo": "っじぇお", "jjo": "っじょ", "jju": "っじゅ",
    "jjeu": "っじぇう", "jji": "っじ", "jjae": "っじゃえ", "jje": "っじぇ", "jjoe": "っじょえ",
    "jjwi": "ｊｊうぃ", "jjya": "っじゃ", "jjyeo": "っじぇお", "jjyo": "っじょ", "jjyu": "っじゅ",
    "jjyae": "っじゃえ", "jjye": "っじぇ", "jjwa": "ｊｊわ", "jjwae": "ｊｊわえ", "jjwo": "ｊｊを",
    "jjwe": "ｊｊうぇ", "jjui": "っじゅい", "cha": "ちゃ", "cheo": "ちぇお", "cho": "ちょ", "chu": "ちゅ",
    "cheu": "ちぇう", "chi": "ち", "chae": "ちゃえ", "che": "ちぇ", "choe": "ちょえ", "chwi": "ｃｈうぃ",
    "chya": "ｃひゃ", "chyeo": "ｃひぇお", "chyo": "ｃひょ", "chyu": "ｃひゅ", "chyae": "ｃひゃえ",
    "chye": "ｃひぇ", "chwa": "ｃｈわ", "chwae": "ｃｈわえ", "chwo": "ｃｈを", "chwe": "ｃｈうぇ",
    "chui": "ちゅい", "sa": "さ", "seo": "せお", "so": "そ", "su": "す", "seu": "せう", "si": "し",
    "sae": "さえ", "se": "せ", "soe": "そえ", "swi": "すぃ", "sya": "しゃ", "syeo": "しぇお",
    "syo": "しょ", "syu": "しゅ", "syae": "しゃえ", "sye": "しぇ", "swa": "すぁ", "swae": "すぁえ",
    "swo": "すぉ", "swe": "すぇ", "sui": "すい", "ssa": "っさ", "sseo": "っせお", "sso": "っそ",
    "ssu": "っす", "sseu": "っせう", "ssi": "っし", "ssae": "っさえ", "sse": "っせ", "ssoe": "っそえ",
    "sswi": "っすぃ", "ssya": "っしゃ", "ssyeo": "っしぇお", "ssyo": "っしょ", "ssyu": "っしゅ",
    "ssyae": "っしゃえ", "ssye": "っしぇ", "sswa": "っすぁ", "sswae": "っすぁえ", "sswo": "っすぉ",
    "sswe": "っすぇ", "ssui": "っすい", "ha": "は", "heo": "へお", "ho": "ほ", "hu": "ふ", "heu": "へう",
    "hi": "ひ", "hae": "はえ", "he": "へ", "hoe": "ほえ", "hwi": "ｈうぃ", "hya": "ひゃ", "hyeo": "ひぇお",
    "hyo": "ひょ", "hyu": "ひゅ", "hyae": "ひゃえ", "hye": "ひぇお", "hwa": "ｈわ", "hwae": "ｈわえ",
    "hwo": "ｈを", "hwe": "ｈうぇ", "hui": "ふい", "na": "な", "neo": "ねお", "no": "の", "nu": "ぬ",
    "neu": "ねう", "ni": "に", "nae": "なえ", "ne": "ね", "noe": "のえ", "nwi": "んうぃ", "nya": "にゃ",
    "nyeo": "にぇお", "nyo": "にょ", "nyu": "にゅ", "nyae": "にゃえ", "nye": "にぇ", "nwa": "んわ",
    "nwae": "んわえ", "nwo": "んを", "nwe": "んうぇ", "nui": "ぬい", "ma": "ま", "meo": "めお",
    "mo": "も", "mu": "む", "meu": "めう", "mi": "み", "mae": "まえ", "me": "め", "moe": "もえ",
    "mwi": "ｍうぃ", "mya": "みゃ", "myeo": "みぇお", "myo": "みょ", "myu": "みゅ", "myae": "みゃえ",
    "mye": "みぇ", "mwa": "ｍわ", "mwae": "ｍわえ", "mwo": "ｍを", "mwe": "ｍうぇ", "mui": "むい",
    "ra": "ら", "reo": "れお", "ro": "ろ", "ru": "る", "reu": "れう", "ri": "り", "rae": "らえ",
    "re": "れ", "roe": "ろえ", "rwi": "ｒうぃ", "rya": "りゃ", "ryeo": "りぇお", "ryo": "りょ",
    "ryu": "りゅ", "ryae": "りゃえ", "rye": "りぇ", "rwa": "ｒわ", "rwae": "ｒわえ", "rwo": "ｒを",
    "rwe": "ｒうぇ", "rui": "るい", "la": "ぁ", "leo": "ぇお", "lo": "ぉ", "lu": "ぅ", "leu": "ぇう",
    "li": "ぃ", "lae": "ぁえ", "le": "ぇ", "loe": "ぉえ", "lwi": "ｌうぃ", "lya": "ゃ", "lyeo": "ぇお",
    "lyo": "ょ", "lyu": "ゅ", "lyae": "ゃえ", "lye": "ぇ", "lwa": "ゎ", "lwae": "ゎえ", "lwo": "ｌを",
    "lwe": "ｌうぇ", "lui": "ぅい", "g": "ｇ", "kk": "ｋｋ", "ks": "ｋｓ", "n": "ｎ", "nj": "んｊ",
    "nh": "んｈ", "d": "ｄ", "r": "ｒ", "lg": "ｌｇ", "lm": "ｌｍ", "lb": "ｌｂ", "ls": "ｌｓ",
    "lt": "ｌｔ", "lp": "ｌｐ", "lh": "ｌｈ", "m": "ｍ", "b": "ｂ", "ps": "ｐｓ", "s": "ｓ", "ss": "ｓｓ",
    "ng": "んｇ", "j": "ｊ", "ch": "ｃｈ", "k": "ｋ", "t": "ｔ", "p": "ｐ", "h": "ｈ", "kt": "ｋｔ",
    "nt": "んｔ", "l": "ｌ", "lk": "ｌｋ", "pt": "ｐｔ", "": "", "ppa": "っぱ", "ppeo": "っぺお",
    "ppo": "っぽ", "ppu": "っぷ", "ppeu": "っぺう", "ppi": "っぴ", "ppae": "っぱえ", "ppe": "っぺ",
    "ppoe": "っぽえ", "ppwi": "ｐｐうぃ", "ppya": "っぴゃ", "ppyeo": "っぴぇお", "ppyo": "っぴょ",
    "ppyu": "っぴゅ", "ppyae": "っぴゃえ", "ppye": "っぴぇ", "ppwa": "ｐｐわ", "ppwae": "ｐｐわえ",
    "ppwo": "ｐｐを", "ppwe": "ｐｐうぇ", "ppui": "っぷい",
}

delim = "\t"
nl = "\n"
w_type = "固有名詞"

vowels = ["a", "i", "u", "e", "o"]


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


def main():
    output_tsv()


def romaji_to_jpinput(_str):
    split = 0
    ret = ""
    d = False
    for i in range(0, len(_str)):
        for j in range(0, len(vowels)):
            if _str[-i - 1] == vowels[j] and not d:
                split = len(_str) - i
                d = True
                break
    if 0 < split:
        ret += rr_to_jp[_str[0:split]]
    if split < len(_str):
        ret += rr_to_jp[_str[split:len(_str)]]
    return ret


def output_tsv():
    f = open("romanized_hangul_typerr.txt", "w", encoding="utf-16le")
    f.write('\ufeff')
    for vi in range(0, len(vowel_rr)):
        for ci in range(0, len(consonant_rr)):
            for bi in range(0, len(batchim_wv_rr)):
                h_uni = hangul_unicode(ci, vi, bi)
                hp1 = hangul_pronounce(h_uni, False)
                hp2 = hangul_pronounce(h_uni, True)
                _str = romaji_to_jpinput(hp1) + delim + str(chr(h_uni)) + delim + w_type + nl
                if romaji_to_jpinput(hp1)[-1] == "ｎ":
                    _str += romaji_to_jpinput(hp1).replace("ｎ", "ん") + delim + str(chr(h_uni)) + delim + w_type + nl
                if hp1 != hp2:
                    _str += romaji_to_jpinput(hp2) + delim + str(chr(h_uni)) + delim + w_type + nl
                    if romaji_to_jpinput(hp2)[-1] == "ｎ":
                        _str += romaji_to_jpinput(hp2).replace("ｎ", "ん") + delim + str(chr(h_uni)) + delim + w_type + nl
                f.write(_str)
    # 特殊ケース 短母音
    f.write("あ" + delim + "ㅇ" + delim + w_type + nl)
    f.write("い" + delim + "ㅇ" + delim + w_type + nl)
    f.write("う" + delim + "ㅇ" + delim + w_type + nl)
    f.write("え" + delim + "ㅇ" + delim + w_type + nl)
    f.write("お" + delim + "ㅇ" + delim + w_type + nl)  # ㅇㅈ インジョンを いｊで出せるようにする
    f.write("あ" + delim + "ㅏ" + delim + w_type + nl)
    f.write("えお" + delim + "ㅓ" + delim + w_type + nl)
    f.write("お" + delim + "ㅗ" + delim + w_type + nl)
    f.write("う" + delim + "ㅜ" + delim + w_type + nl)
    f.write("えう" + delim + "ㅡ" + delim + w_type + nl)
    f.write("い" + delim + "ㅣ" + delim + w_type + nl)
    f.write("あえ" + delim + "ㅐ" + delim + w_type + nl)
    f.write("え" + delim + "ㅔ" + delim + w_type + nl)
    f.write("おえ" + delim + "ㅚ" + delim + w_type + nl)
    f.write("うぃ" + delim + "ㅟ" + delim + w_type + nl)
    # 特殊ケース 二重母音
    f.write("や" + delim + "ㅑ" + delim + w_type + nl)
    f.write("いぇお" + delim + "ㅕ" + delim + w_type + nl)
    f.write("よ" + delim + "ㅛ" + delim + w_type + nl)
    f.write("ゆ" + delim + "ㅠ" + delim + w_type + nl)
    f.write("やえ" + delim + "ㅒ" + delim + w_type + nl)
    f.write("いぇ" + delim + "ㅖ" + delim + w_type + nl)
    f.write("わ" + delim + "ㅘ" + delim + w_type + nl)
    f.write("わえ" + delim + "ㅙ" + delim + w_type + nl)
    f.write("を" + delim + "ㅝ" + delim + w_type + nl)
    f.write("うぇ" + delim + "ㅞ" + delim + w_type + nl)
    f.write("うい" + delim + "ㅢ" + delim + w_type + nl)
    # 特殊ケース 子音
    f.write("ｇ" + delim + "ㄱ" + delim + w_type + nl)
    f.write("ｋ" + delim + "ㄱ" + delim + w_type + nl)
    f.write("ｋｋ" + delim + "ㄲ" + delim + w_type + nl)
    f.write("ｋ" + delim + "ㄲ" + delim + w_type + nl)
    f.write("ｇｇ" + delim + "ㄲ" + delim + w_type + nl)
    f.write("ｄ" + delim + "ㄷ" + delim + w_type + nl)
    f.write("ｔ" + delim + "ㄷ" + delim + w_type + nl)
    f.write("ｔｔ" + delim + "ㄸ" + delim + w_type + nl)
    f.write("ｔ" + delim + "ㅌ" + delim + w_type + nl)
    f.write("ｂ" + delim + "ㅂ" + delim + w_type + nl)
    f.write("ｐ" + delim + "ㅂ" + delim + w_type + nl)
    f.write("ｐｐ" + delim + "ㅃ" + delim + w_type + nl)
    f.write("ｐ" + delim + "ㅍ" + delim + w_type + nl)
    f.write("ｊ" + delim + "ㅈ" + delim + w_type + nl)
    f.write("ｊｊ" + delim + "ㅉ" + delim + w_type + nl)
    f.write("ｃｈ" + delim + "ㅊ" + delim + w_type + nl)
    f.write("ｓ" + delim + "ㅅ" + delim + w_type + nl)
    f.write("ｓｓ" + delim + "ㅆ" + delim + w_type + nl)
    f.write("ｈ" + delim + "ㅎ" + delim + w_type + nl)
    f.write("ｎ" + delim + "ㄴ" + delim + w_type + nl)
    f.write("ん" + delim + "ㄴ" + delim + w_type + nl)
    f.write("ｍ" + delim + "ㅁ" + delim + w_type + nl)
    f.write("ｒ" + delim + "ㄹ" + delim + w_type + nl)
    f.write("ｌ" + delim + "ㄹ" + delim + w_type + nl)
    # 特殊ケース 二重パッチム
    f.write("ｇｓ" + delim + "ㄳ" + delim + w_type + nl)
    f.write("ｌｇ" + delim + "ㄺ" + delim + w_type + nl)
    f.write("んｊ" + delim + "ㄵ" + delim + w_type + nl)
    f.write("んｈ" + delim + "ㄶ" + delim + w_type + nl)
    f.write("ｌｓ" + delim + "ㄽ" + delim + w_type + nl)
    f.write("ｌｔ" + delim + "ㄾ" + delim + w_type + nl)
    f.write("ｌｈ" + delim + "ㅀ" + delim + w_type + nl)
    f.write("ｌｂ" + delim + "ㄼ" + delim + w_type + nl)
    f.write("ｌｍ" + delim + "ㄻ" + delim + w_type + nl)
    f.write("ｂｓ" + delim + "ㅄ" + delim + w_type + nl)
    f.write("ｌｐ" + delim + "ㄿ" + delim + w_type + nl)
    f.close()


if __name__ == '__main__':
    main()

