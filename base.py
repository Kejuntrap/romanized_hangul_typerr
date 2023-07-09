import os
from typing import TextIO

NL = "\n"
W_TYPE = "固有名詞"
DELIM = "\t"
FILE_ENCODING = "utf-16le"
COMMENT = '#'

HANGEUL_VOWEL = [
    "ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅗ", "ㅘ", "ㅙ", "ㅚ", "ㅛ", "ㅜ", "ㅝ", "ㅞ", "ㅟ", "ㅠ", "ㅡ", "ㅢ", "ㅣ"
]

VOWEL_RR = ["a", "ae", "ya", "yae", "eo", "e", "yeo", "ye", "o", "wa", "wae", "oe", "yo", "u", "wo", "we", "wi", "yu",
            "eu", "ui", "i"]

CONSONANT_RR = ["g", "kk", "n", "d", "tt", "r", "m", "b", "pp", "s", "ss", "", "j", "jj", "ch", "k", "t", "p", "h"]
HANGEUL_CONSONANT = [
    "ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"
]

BATCHIM_WOV_RR = ["", "k", "k", "kt", "n", "nt", "nh", "t", "l", "lk", "lm", "lp", "lt", "lt", "lp", "lh", "m", "p",
                  "pt", "t", "t", "ng", "t", "t", "k", "t", "p", "h"]
BATCHIM_WV_RR = ["", "g", "kk", "ks", "n", "nj", "nh", "d", "r", "lg", "lm", "lb", "ls", "lt", "lp", "lh", "m", "b",
                 "ps", "s", "ss", "ng", "j", "ch", "k", "t", "p", "h"]
HANGEUL_BATCHIM = [
    [""], ["ᆨ", "ᄀ"], ["ᆩ", "ᄁ"], ["ᆪ"], ["ᆫ", "ᄂ"], ["ᆬ", "ᅜ"], ["ᆭ", "ᅝ"], ["ᆮ", "ᄃ"], ["ᆯ", "ᄅ"], ["ᆰ"], ["ᆱ"],
    ["ᆲ"], ["ᆳ"],
    ["ᆴ"], ["ᆵ"], ["ᆶ", "ᄚ"], ["ᆷ", "ᄆ"], ["ᆸ", "ᄇ"], ["ᆹ", "ᄡ"], ["ᆺ", "ᄉ"], ["ᆻ", "ᄊ"], ["ᆼ", "ᄋ"], ["ᆽ", "ᄌ"],
    ["ᆾ", "ᄎ"],
    ["ᆿ", "ᄏ"], ["ᇀ", "ᄐ"], ["ᇁ", "ᄑ"], ["ᇂ", "ᄒ"]
]

RR_TO_JP = {
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
    "ppwo": "ｐｐを", "ppwe": "ｐｐうぇ", "ppui": "っぷい", "tt": "ｔｔ", "pp": "ｐｐ", "jj": "ｊｊ"
}

VOWELS = ["a", "i", "u", "e", "o"]

VOWEL_VOLUME = [
    ["yae", "yeo", "wae"],
    ["ae", "ya", "eo", "ye", "wa", "oe", "yo", "wo", "we", "wi", "yu", "eu", "ui"],
    ["a", "e", "o", "u", "i"]
]

IRREGULAR_VOWELS = ["l", "p", "k", "m", "j", "t", "r", "s", "h", "g", "b", "d", "c"]

HAN_ZEN_VOWELS = {"l": "ｌ", "p": "ｐ", "k": "ｋ", "m": "ｍ", "j": "ｊ", "t": "ｔ", "r": "ｒ", "s": "ｓ", "h": "ｈ", "g": "ｇ", "b": "ｂ", "d": "ｄ", "c": "ｃ"}


def convert_romaji_jp_type(_str):  # ローマ字表記を日本語入力に変換
    _ret_str = ""
    _pointer = 0
    n_flag = False
    for i in range(0, len(_str)):
        if _str[i] in VOWELS:
            n_flag = False
            if _str[_pointer:i + 1] in RR_TO_JP:
                _ret_str += RR_TO_JP[_str[_pointer:i + 1]]
                _pointer = i + 1
            else:  # 未登録の対応があったら
                if _str[_pointer:i + 1][0] in IRREGULAR_VOWELS:  # 未登録はl,p,k,m始まりらしい
                    _ret_str += HAN_ZEN_VOWELS[_str[_pointer:i + 1][0]]
                    _pointer += 1
                else:
                    print("!!", _str)
                    break
                if _str[_pointer:i + 1] in RR_TO_JP:
                    _ret_str += RR_TO_JP[_str[_pointer:i + 1]]
                    _pointer = i + 1
        elif _str[i] == 'n':
            if n_flag:  # nn
                _ret_str += "ん"
                n_flag = False
                _pointer = i + 1
            else:  # hajimete n flag
                n_flag = True
                if _str[_pointer:i + 1] in RR_TO_JP:
                    _ret_str += RR_TO_JP[_str[_pointer:i]]
                else:
                    if _pointer + 1 == i:
                        _ret_str += HAN_ZEN_VOWELS[_str[_pointer:i]]
                    else:
                        _ret_str += convert_romaji_jp_type(_str[_pointer:i])
                _pointer = i
        elif _str[i] != 'n':
            if n_flag:
                _ret_str += "ん"
                n_flag = False
                _pointer = i

    if _pointer < len(_str):
        t_pointer = _pointer
        for i in range(t_pointer, len(_str)):
            if _str[i:len(_str)] in RR_TO_JP:
                _ret_str += RR_TO_JP[_str[i:len(_str)]]
                break
            else:  # 未登録の対応があったら
                if _str[i:len(_str)] in IRREGULAR_VOWELS:
                    _ret_str += HAN_ZEN_VOWELS[_str[_pointer]]
    return _ret_str


def hangul_unicode(_c, _v, _b):
    return 0xAC00 + _c * 0x24C + _v * 0x1C + _b


def hangul_pronounce(code, _next_vowel):
    code -= 0xAC00
    _c = code // 0x24C
    _v = (code - _c * 0x24C) // 0x1C
    _b = code % 0x1C
    if _next_vowel:
        return CONSONANT_RR[_c] + VOWEL_RR[_v] + BATCHIM_WV_RR[_b]
    else:
        return CONSONANT_RR[_c] + VOWEL_RR[_v] + BATCHIM_WOV_RR[_b]


def rr2k(_str):
    _ret = ""
    for i in range(0, len(_str)):
        if i < len(_str) - 1:
            if 0xAC00 + 0x24C * 11 <= ord(_str[i + 1]) < 0xAC00 + 0x24C * 12:
                _ret += hangul_pronounce(ord(_str[i]), True)
            else:
                _ret += hangul_pronounce(ord(_str[i]), False)
        else:
            _ret += hangul_pronounce(ord(_str[i]), False)
    return _ret


def k_j(_str):  # ハングルから日本語の入力形式
    return convert_romaji_jp_type(rr2k(_str))


def file_check(x):
    if not os.path.exists(x):
        return None
    else:
        return open(x, 'r', encoding=FILE_ENCODING)  # return an open file handle


def dictionary_word_maker(x):
    result = ""
    tmp = ""
    last_index = 0
    for i in range(0,len(x)):
        if x[i] in HANGEUL_BATCHIM or x[i] in HANGEUL_VOWEL or x[i] in HANGEUL_CONSONANT or 0xAC00 <= ord(x[i]) <= 0xD7A3:
            tmp += x[i]
        else:
            result += k_j(tmp)
            tmp = ""
            result += x[i]
    if tmp != "":
        result += k_j(tmp)
    return result


class DictionaryWriter:
    output_filename: str
    writer: TextIO
    encoding: str

    def init(self, _file_name, _enc):
        self.output_filename = _file_name
        self.encoding = _enc
        self.writer = open(self.output_filename, 'w', encoding=self.encoding)
        if self.encoding == FILE_ENCODING:
            self.writer.write('\ufeff')  # magic number cf:bom

    def w_str(self, _str):
        self.writer.write(_str)

    def wl(self, _ary, _delim):
        _str = ""
        for i in range(0, len(_ary) - 1):
            _str += _ary[i] + _delim
        _str += _ary[len(_ary) - 1] + NL
        self.writer.write(_str)

    def close(self):
        self.writer.close()
