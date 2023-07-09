import operator
import os.path
import base as b

accum_sum = 0
accum = 0
cover_percentage = 1.00
rensetsu = {}
refined_rensetsu = {}
word_bank = {}


def main():
    global accum_sum
    global accum
    dt = read_ner_dataset()
    generate_multi_word_freq_dict(dt)

    for a in rensetsu:
        if rensetsu[a] > 0:
            refined_rensetsu[a] = rensetsu[a]
            accum_sum += rensetsu[a]
    s_res = sorted(refined_rensetsu.items(), key=operator.itemgetter(1), reverse=True)
    output_from_copus(s_res)
    print("done")


def output_from_copus(s_res):
    global accum_sum
    global accum
    f: b.DictionaryWriter = b.DictionaryWriter()
    f.init("../romanized_hangul_multi_from_corpus.txt", b.FILE_ENCODING)
    for i in range(0, len(s_res)):
        accum += s_res[i][1]
        if accum / accum_sum <= cover_percentage:
            _pronounce = b.hangul_pronounce(ord(s_res[i][0][0]), True) + b.hangul_pronounce(ord(s_res[i][0][1]), False)
            _jp_type = b.convert_romaji_jp_type(_pronounce)
            f.wl([_jp_type, s_res[i][0], b.W_TYPE], b.DELIM)
    f.close()


def generate_multi_word_freq_dict(_dataset):
    for i in range(0, len(_dataset)):
        for j in range(0, len(_dataset[i][0]) - 1):
            _tmp_str = _dataset[i][0][j:j + 2]
            if (0xAC00 + 0x24C * 11 <= ord(_tmp_str[-1]) < 0xAC00 + 0x24C * 12) and ((ord(_tmp_str[0]) - 0xAC00) % 0x1C != 0):
                if _tmp_str not in rensetsu:
                    rensetsu[_tmp_str] = _dataset[i][1]
                else:
                    rensetsu[_tmp_str] += _dataset[i][1]


def read_ner_dataset():
    word_count = 0
    word_species = 0
    for i in range(0, 50000):
        file_name = str(i).rjust(5, '0') + "_NER.txt"
        if os.path.isfile("../NER/" + file_name):
            f = open("../NER/" + file_name, encoding="utf-8")
            s = f.readlines()
            # print(file_name,len(s))
            f.close()
            for _lines in range(0, len(s)):
                if s[_lines][0] != '#':
                    w = s[_lines].split("\t")
                    if len(w) >= 4 and (w[2] == "NNP" or w[2] == "NNG"):  # NNGが一般名詞　NNPが固有名詞
                        if len(w[0]) >= 2:
                            if w[0] not in word_bank:
                                word_bank[w[0]] = 1
                                word_species += 1
                            else:
                                word_bank[w[0]] += 1
                            word_count += 1
    # print(word_species, word_count)
    s_res = sorted(word_bank.items(), key=operator.itemgetter(1), reverse=True)
    return s_res


if __name__ == '__main__':
    main()
