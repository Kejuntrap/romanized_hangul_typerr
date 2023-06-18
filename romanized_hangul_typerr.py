import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

hangul_vowel = [
    "ㅏ","ㅐ","ㅑ","ㅒ","ㅓ","ㅔ","ㅕ","ㅖ","ㅗ","ㅘ","ㅙ","ㅚ","ㅛ","ㅜ","ㅝ","ㅞ","ㅟ","ㅠ","ㅡ","ㅢ","ㅣ"
]
vowels = ["a", "i", "u", "e", "o"]
vowel_rr = ["a", "ae", "ya", "yae", "eo", "e", "yeo", "ye", "o", "wa", "wae", "oe", "yo", "u", "wo", "we", "wi", "yu",
            "eu", "ui", "i"]

consonant_rr = ["g", "kk", "n", "d", "tt", "r", "m", "b", "pp", "s", "ss", "", "j", "jj", "ch", "k", "t", "p", "h"]
hangul_consonant = [
    "ㄱ","ㄲ","ㄴ","ㄷ","ㄸ","ㄹ","ㅁ","ㅂ","ㅃ","ㅅ","ㅆ","ㅇ","ㅈ","ㅉ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ"
]

batchim_wov_rr = ["", "k", "k", "kt", "n", "nt", "nh", "t", "l", "lk", "lm", "lp", "lt", "lt", "lp", "lh", "m", "p",
                  "pt", "t", "t", "ng", "t", "t", "k", "t", "p", "h"]
batchim_wv_rr = ["", "g", "kk", "ks", "n", "nj", "nh", "d", "r", "lg", "lm", "lb", "ls", "lt", "lp", "lh", "m", "b",
                 "ps", "s", "ss", "ng", "j", "ch", "k", "t", "p", "h"]
hangul_batchim = [
    [""],["ᆨ","ᄀ"],["ᆩ","ᄁ"],["ᆪ"],["ᆫ","ᄂ"],["ᆬ","ᅜ"],["ᆭ","ᅝ"],["ᆮ","ᄃ"],["ᆯ","ᄅ"],["ᆰ"],["ᆱ"],["ᆲ"],["ᆳ"],
    ["ᆴ"],["ᆵ"],["ᆶ","ᄚ"],["ᆷ","ᄆ"],["ᆸ","ᄇ"],["ᆹ","ᄡ"],["ᆺ","ᄉ"],["ᆻ","ᄊ"],["ᆼ","ᄋ"],["ᆽ","ᄌ"],["ᆾ","ᄎ"],
    ["ᆿ","ᄏ"],["ᇀ","ᄐ"],["ᇁ","ᄑ"],["ᇂ","ᄒ"]
]

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
    "ppwo": "ｐｐを", "ppwe": "ｐｐうぇ", "ppui": "っぷい","tt":"ｔｔ","pp":"ｐｐ","jj":"ｊｊ"
}

# keyは　ハングルのアルファベット表記＋日本語入力＋ハングル
duplication_memorize = {}   # 同じハングルと読みが登録されていないか?


delim = "\t"
nl = "\n"
w_type = "固有名詞"


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
    print(len(duplication_memorize))


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

                if hp1+romaji_to_jpinput(hp1)+str(chr(h_uni)) not in duplication_memorize:
                    _str = romaji_to_jpinput(hp1) + delim + str(chr(h_uni)) + delim + w_type + nl
                    duplication_memorize[hp1+romaji_to_jpinput(hp1)+str(chr(h_uni))] = 1

                if romaji_to_jpinput(hp1)[-1] == "ｎ" and hp1+romaji_to_jpinput(hp1).replace("ｎ", "ん")+str(chr(h_uni)) not in duplication_memorize:
                    _str += romaji_to_jpinput(hp1).replace("ｎ", "ん") + delim + str(chr(h_uni)) + delim + w_type + nl    # ぱｎ(판)のように最後がｎで終わるやつがんに変換されても出るようにする
                    duplication_memorize[hp1+romaji_to_jpinput(hp1).replace("ｎ", "ん")+str(chr(h_uni))] = 1

                if hp1 != hp2 and hp2+romaji_to_jpinput(hp2)+str(chr(h_uni)) not in duplication_memorize:      # 後にくるハングルで読みが変わるやつはそれも登録する
                    _str += romaji_to_jpinput(hp2) + delim + str(chr(h_uni)) + delim + w_type + nl
                    duplication_memorize[hp2+romaji_to_jpinput(hp2)+str(chr(h_uni))] = 1
                    if romaji_to_jpinput(hp2)[-1] == "ｎ" and hp2+romaji_to_jpinput(hp2).replace("ｎ", "ん")+str(chr(h_uni)) not in duplication_memorize:
                        _str += romaji_to_jpinput(hp2).replace("ｎ", "ん") + delim + str(chr(h_uni)) + delim + w_type + nl    # ぱｎ(판)のように最後がｎで終わるやつがんに変換されても出るようにする
                        duplication_memorize[hp2+romaji_to_jpinput(hp2).replace("ｎ", "ん")+str(chr(h_uni))] = 1

                if len(_str) > 0:
                    f.write(_str)

    # 母音ㅏやㅗなど ㅇをngと母音で出せるようにする ㅇㅈをいｊで出せるようにする
    for i in range(0,len(hangul_vowel)):
        if vowel_rr[i] + romaji_to_jpinput(vowel_rr[i]) + hangul_vowel[i] not in duplication_memorize:
            f.write(romaji_to_jpinput(vowel_rr[i]) + delim + hangul_vowel[i] + delim + w_type + nl)
            duplication_memorize[vowel_rr[i] + romaji_to_jpinput(vowel_rr[i]) + hangul_vowel[i]] = 1

        if vowel_rr[i] +romaji_to_jpinput(vowel_rr[i]) + "ㅇ" not in duplication_memorize:
            f.write(romaji_to_jpinput(vowel_rr[i]) + delim + "ㅇ" + delim + w_type + nl)
            duplication_memorize[vowel_rr[i] + romaji_to_jpinput(vowel_rr[i])+ "ㅇ"] = 1

        f.write("んｇ" + delim + "ㅇ" + delim + w_type + nl)  # ㅇㅈ インジョンを いｊで出せるようにする
        duplication_memorize["ngんｇㅇ"] = 1


    # 子音
    for i in range(0,len(hangul_consonant)):
        if len(romaji_to_jpinput(consonant_rr[i])) > 0 and consonant_rr[i]+romaji_to_jpinput(consonant_rr[i])+hangul_consonant[i] not in duplication_memorize: # 無音のㅇを登録するのはあまりよろしくない
            f.write(romaji_to_jpinput(consonant_rr[i]) + delim + hangul_consonant[i] + delim + w_type + nl)
            duplication_memorize[consonant_rr[i]+romaji_to_jpinput(consonant_rr[i])+hangul_consonant[i]] = 1

    # パッチム
    for i in range(1,len(hangul_batchim)):  # 0はパッチムがつかないハングル用なので
        for j in range(0,len(hangul_batchim[i])):
            if batchim_wov_rr[i]+romaji_to_jpinput(batchim_wov_rr[i])+hangul_batchim[i][j] not in duplication_memorize:
                f.write(romaji_to_jpinput(batchim_wov_rr[i]) + delim + hangul_batchim[i][j] + delim + w_type + nl)
                duplication_memorize[batchim_wov_rr[i]+romaji_to_jpinput(batchim_wov_rr[i])+hangul_batchim[i][j]] = 1

            if batchim_wv_rr[i]+romaji_to_jpinput(batchim_wv_rr[i])+hangul_batchim[i][j] not in duplication_memorize:
                f.write(romaji_to_jpinput(batchim_wv_rr[i]) + delim + hangul_batchim[i][j] + delim + w_type + nl)
                duplication_memorize[batchim_wv_rr[i]+romaji_to_jpinput(batchim_wv_rr[i])+hangul_batchim[i][j]] = 1

    f.close()


if __name__ == '__main__':
    main()

