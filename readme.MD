# romanized hangul iput

韓国語からラテン文字への転写の方法はいくつかあるが，その中で最もよく使われている文化観光部2000年式(Revised Romanization of Korean; RR式)を用いて韓国語をローマ字入力できるようにユーザー登録辞書の形でそれを実現した。

[文化観光部2000年式(RR式)](https://ja.wikipedia.org/wiki/%E6%96%87%E5%8C%96%E8%A6%B3%E5%85%89%E9%83%A82000%E5%B9%B4%E5%BC%8F)

韓国語のラテン文字転写方法として，RR式についで有名と思われるのが，マッキューン＝ライシャワー式やイェール式などがある。

## example

`안녕하세요` <- `an nyeong ha se yo`(こんにちは)

`이 상혁` <- `i sang hyeok`(Faker)

`김 혁규` <- `gim hyeok gyu`(Deft)

`중요한 건 꺾이지 않는 마움` <- `jung yo han geon kkeokk i ji anh neun ma um`(The most important is the unbreakable spirit.)

`톡! 톡! 톡!` <- `tok! tok! tok!`

## how to use

`romanized_hangul_typerr.py`を実行し出力されたtxtファイルを

IMEのアイコン(「A」とか「あ」のやつ)を右クリックして単語の追加

ユーザー辞書ツール -> ツール -> テキストファイルからの登録する

このリポジトリにある`romanized_hangul_typerr.txt`はすでに`romanized_hangul_typerr.py`を実行して出力したものなのでテキストファイルをダウンロードしてIMEに追加することも可能。


## features

`ㅇ`はパッチムで`ng`と発音する以外は無音であるので，`ㅇ`は特別に「あ，い，う，え，お，んｇ」で出せるようになっている。

## how to run

開発はpython3(3.9.12)

外部のライブラリを使用していない為
動作確認はしていないが3.6くらいでも動くはず

## licence

MIT Licence
