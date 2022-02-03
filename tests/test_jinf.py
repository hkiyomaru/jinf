import json
import tempfile

import pytest
from pyknp import Morpheme

from jinf import InflectionForm, Jinf
from jinf.inflection_form import INFECTION_FORMS


def test_init():
    _ = Jinf()


def test_init_error_0():
    with pytest.raises(FileNotFoundError):
        _ = Jinf("foo")


def test_init_error_1():
    with tempfile.NamedTemporaryFile("wt", encoding="utf-8") as f:
        f.write("{")  # invalid json
        with pytest.raises(json.decoder.JSONDecodeError):
            _ = Jinf(f.name)


@pytest.mark.parametrize(
    "m, inf_forms, infs",
    [
        (
            Morpheme('食べる たべる 食べる 動詞 2 * 0 母音動詞 1 基本形 2 "代表表記:食べる/たべる ドメイン:料理・食事"'),
            ("語幹", "基本形", "未然形", "意志形"),
            ("食べ", "食べる", "食べ", "食べよう"),
        ),
        (
            Morpheme('決める きめる 決める 動詞 2 * 0 母音動詞 1 基本形 2 "代表表記:決める/きめる 自他動詞:自:決まる/きまる"'),
            ("語幹", "基本形", "未然形", "意志形"),
            ("決め", "決める", "決め", "決めよう"),
        ),
        (
            Morpheme('書ける かける 書ける 動詞 2 * 0 母音動詞 1 基本形 2 "代表表記:書ける/かける 可能動詞:書く/かく 補文ト"'),
            ("語幹", "基本形", "未然形", "意志形"),
            ("書け", "書ける", "書け", "書けよう"),
        ),
        (
            Morpheme('咲く さく 咲く 動詞 2 * 0 子音動詞カ行 2 基本形 2 "代表表記:咲く/さく"'),
            ("語幹", "基本形", "未然形", "意志形"),
            ("咲", "咲く", "咲か", "咲こう"),
        ),
        (
            Morpheme(
                '行く いく 行く 動詞 2 * 0 子音動詞カ行促音便形 3 基本形 2 "代表表記:行く/いく ドメイン:交通 反義:動詞:帰る/かえる 付属動詞候補（タ系）"'
            ),
            ("語幹", "基本形", "未然形", "意志形"),
            ("行", "行く", "行か", "行こう"),
        ),
        (
            Morpheme(
                '騒ぐ さわぐ 騒ぐ 動詞 2 * 0 子音動詞ガ行 4 基本形 2 "代表表記:騒ぐ/さわぐ 補文ト 形容詞派生:騒がしい/さわがしい"'
            ),
            ("語幹", "基本形", "未然形", "意志形"),
            ("騒", "騒ぐ", "騒が", "騒ごう"),
        ),
        (
            Morpheme('許す ゆるす 許す 動詞 2 * 0 子音動詞サ行 5 基本形 2 "代表表記:許す/ゆるす"'),
            ("語幹", "基本形", "未然形", "意志形"),
            ("許", "許す", "許さ", "許そう"),
        ),
        (
            Morpheme('待つ まつ 待つ 動詞 2 * 0 子音動詞タ行 6 基本形 2 "代表表記:待つ/まつ"'),
            ("語幹", "基本形", "未然形", "意志形"),
            ("待", "待つ", "待た", "待とう"),
        ),
        (
            Morpheme(
                '死ぬ しぬ 死ぬ 動詞 2 * 0 子音動詞ナ行 7 基本形 2 "代表表記:死ぬ/しぬ ドメイン:家庭・暮らし 反義:動詞:産まれる/うまれる;動詞:生まれる/うまれる"'
            ),
            ("語幹", "基本形", "未然形", "意志形"),
            ("死", "死ぬ", "死な", "死のう"),
        ),
        (
            Morpheme('遊ぶ あそぶ 遊ぶ 動詞 2 * 0 子音動詞バ行 8 基本形 2 "代表表記:遊ぶ/あそぶ ドメイン:レクリエーション"'),
            ("語幹", "基本形", "未然形", "意志形"),
            ("遊", "遊ぶ", "遊ば", "遊ぼう"),
        ),
        (
            Morpheme('和む なごむ 和む 動詞 2 * 0 子音動詞マ行 9 基本形 2 "代表表記:和む/なごむ"'),
            ("語幹", "基本形", "未然形", "意志形"),
            ("和", "和む", "和ま", "和もう"),
        ),
        (
            Morpheme(
                '降る ふる 降る 動詞 2 * 0 子音動詞ラ行 10 基本形 2 "代表表記:降る/ふる 反義:動詞:止む/やむ;動詞:上がる/あがる"'
            ),
            ("語幹", "基本形", "未然形", "意志形"),
            ("降", "降る", "降ら", "降ろう"),
        ),
        (
            Morpheme(
                '下さい ください 下さる 動詞 2 * 0 子音動詞ラ行イ形 11 命令形 6 "代表表記:下さる/くださる 付属動詞候補（タ系） 尊敬動詞:与える/あたえる;くれる/くれる 長音挿入可"'
            ),
            ("語幹", "基本形", "未然形", "意志形"),
            ("下さ", "下さる", "下さら", "下さろう"),
        ),
        (
            Morpheme(
                '買った かった 買う 動詞 2 * 0 子音動詞ワ行 12 タ形 10 "代表表記:買う/かう ドメイン:家庭・暮らし;ビジネス 反義:動詞:売る/うる"'
            ),
            ("語幹", "基本形", "未然形", "意志形"),
            ("買", "買う", "買わ", "買おう"),
        ),
        (
            Morpheme(
                '問う とう 問う 動詞 2 * 0 子音動詞ワ行文語音便形 13 基本形 2 "代表表記:問う/とう 反義:動詞:答える/こたえる"'
            ),
            ("語幹", "基本形", "未然形", "意志形"),
            ("問", "問う", "問わ", "問おう"),
        ),
        (
            Morpheme('くる くる くる 動詞 2 * 0 カ変動詞 14 基本形 2 "代表表記:来る/くる 反義:動詞:帰る/かえる"'),
            ("語幹", "基本形", "未然形", "意志形"),
            ("", "くる", "こ", "こよう"),
        ),
        (
            Morpheme('来る 来る 来る 動詞 2 * 0 カ変動詞来 15 基本形 2 "代表表記:来る/くる 反義:動詞:帰る/かえる"'),
            ("語幹", "基本形", "未然形", "意志形"),
            ("", "来る", "来", "来よう"),
        ),
        (
            Morpheme(
                'する する する 動詞 2 * 0 サ変動詞 16 基本形 2 "代表表記:する/する 自他動詞:自:成る/なる 付属動詞候補（基本）"'
            ),
            ("語幹", "基本形", "未然形", "意志形"),
            ("", "する", "さ", "しよう"),
        ),
        (
            Morpheme(
                '生ずる しょうずる 生ずる 動詞 2 * 0 ザ変動詞 17 基本形 2 "代表表記:生ずる/しょうずる 自他動詞:同形 同義:動詞:生じる/しょうじる"'
            ),
            ("語幹", "基本形", "未然形", "意志形"),
            ("生", "生ずる", "生ざ", "生じよう"),
        ),
        (
            Morpheme('すごい すごい すごい 形容詞 3 * 0 イ形容詞アウオ段 18 基本形 2 "代表表記:凄い/すごい"'),
            ("語幹", "基本形", "基本推量形", "基本条件形"),
            ("すご", "すごい", "すごかろう", "すごければ"),
        ),
        (
            Morpheme(
                '美しい うつくしい 美しい 形容詞 3 * 0 イ形容詞イ段 19 基本形 2 "代表表記:美しい/うつくしい 反義:形容詞:醜い/みにくい"'
            ),
            ("語幹", "基本形", "基本推量形", "基本条件形"),
            ("美し", "美しい", "美しかろう", "美しければ"),
        ),
        (
            Morpheme(
                '大きい おおきい 大きい 形容詞 3 * 0 イ形容詞イ段特殊 20 基本形 2 "代表表記:大きい/おおきい 反義:形容詞:小さい/ちいさい"'
            ),
            ("語幹", "基本形", "基本推量形", "基本条件形"),
            ("大き", "大きい", "大きかろう", "大きければ"),
        ),
        (
            Morpheme('壮大だ そうだいだ 壮大だ 形容詞 3 * 0 ナ形容詞 21 基本形 2 "代表表記:壮大だ/そうだいだ"'),
            ("語幹", "基本形", "ダ列基本推量形", "ダ列基本条件形"),
            ("壮大", "壮大だ", "壮大だろう", "壮大ならば"),
        ),
        (
            Morpheme(
                '最短だ さいたんだ 最短だ 形容詞 3 * 0 ナノ形容詞 22 基本形 2 "代表表記:最短だ/さいたんだ 反義:形容詞:最長だ/さいちょうだ"'
            ),
            ("語幹", "基本形", "ダ列基本推量形", "ダ列基本条件形"),
            ("最短", "最短だ", "最短だろう", "最短ならば"),
        ),
        (
            Morpheme(
                '同じだ おなじだ 同じだ 形容詞 3 * 0 ナ形容詞特殊 23 基本形 2 "代表表記:同じだ/おなじだ 反義:動詞:違う/ちがう"'
            ),
            ("語幹", "基本形", "ダ列基本推量形", "ダ列基本条件形"),
            ("同じ", "同じだ", "同じだろう", "同じならば"),
        ),
        (
            Morpheme('忸怩たる じくじたる 忸怩たる 形容詞 3 * 0 タル形容詞 24 基本形 2 "代表表記:忸怩たる/じくじたる"'),
            ("語幹", "基本形", "基本連用形"),
            ("忸怩", "忸怩たる", "忸怩と"),
        ),
        (
            Morpheme("だ だ だ 判定詞 4 * 0 判定詞 25 基本形 2 NIL"),
            ("語幹", "基本形", "ダ列基本推量形", "ダ列基本条件形"),
            ("", "だ", "だろう", "ならば"),
        ),
        (
            Morpheme("ぬ ぬ ぬ 助動詞 5 * 0 助動詞ぬ型 27 基本形 2 NIL"),
            ("語幹", "基本形", "基本推量形", "基本条件形"),
            ("", "ぬ", "ぬだろう", "ねば"),
        ),
        (
            Morpheme("だろう だろう だろう 助動詞 5 * 0 助動詞だろう型 28 基本形 2 NIL"),
            ("語幹", "基本形", "ダ列基本省略推量形", "ダ列基本条件形"),
            ("", "だろう", "だろ", "ならば"),
        ),
        (
            Morpheme("そうだ そうだ そうだ 助動詞 5 * 0 助動詞そうだ型 29 基本形 2 NIL"),
            ("語幹", "基本形"),
            ("そう", "そうだ"),
        ),
        (
            Morpheme("べし べし べし 助動詞 5 * 0 助動詞く型 30 基本形 2 NIL"),
            ("語幹", "基本形", "基本連用形"),
            ("べ", "べし", "べく"),
        ),
        (
            Morpheme('ます ます ます 接尾辞 14 動詞性接尾辞 7 動詞性接尾辞ます型 31 基本形 2 "代表表記:ます/ます"'),
            ("語幹", "基本形", "未然形", "意志形"),
            ("", "ます", "ませ", "ましょう"),
        ),
        (
            Morpheme('うる うる うる 接尾辞 14 動詞性接尾辞 7 動詞性接尾辞うる型 32 基本形 2 "代表表記:得る/える"'),
            ("語幹", "基本形", "基本条件形"),
            ("", "うる", "うれば"),
        ),
    ],
)
def test_call(m: Morpheme, inf_forms: list[InflectionForm], infs: list[str]):
    jinf = Jinf()
    for inf, inf_form in zip(infs, inf_forms):
        assert inf == jinf(m, inf_form)


def test_call_error_0():
    jinf = Jinf()
    m = Morpheme('言語 げんご 言語 名詞 6 普通名詞 1 * 0 * 0 "代表表記:言語/げんご カテゴリ:抽象物"')
    with pytest.raises(ValueError):
        jinf(m, "未然形_")  # invalid inflection form


def test_call_error_1():
    jinf = Jinf()
    m = Morpheme('言語 げんご 言語 名詞 6 普通名詞 1 * 0 * 0 "代表表記:言語/げんご カテゴリ:抽象物"')
    with pytest.raises(ValueError):
        jinf(m, 42)  # invalid inflection form


@pytest.mark.parametrize(
    "m",
    [
        Morpheme('言語 げんご 言語 名詞 6 普通名詞 1 * 0 * 0 "代表表記:言語/げんご カテゴリ:抽象物"'),
        Morpheme('こんにちは こんにちは こんにちは 感動詞 12 * 0 * 0 * 0 "代表表記:こんにちは/こんにちは"'),
        Morpheme("。 。 。 特殊 1 句点 1 * 0 * 0 NIL"),
        Morpheme('まさに まさに まさに 副詞 8 * 0 * 0 * 0 "代表表記:正に/まさに"'),
    ],
)
def test_call_error_2(m: Morpheme):
    jinf = Jinf()
    for inf_form in INFECTION_FORMS:
        with pytest.raises(ValueError):
            _ = jinf(m, inf_form)


@pytest.mark.parametrize(
    "m, inf_forms",
    [
        (
            Morpheme('食べる たべる 食べる 動詞 2 * 0 母音動詞 1 基本形 2 "代表表記:食べる/たべる ドメイン:料理・食事"'),
            (
                "デアル列命令形",
                "デアル列基本形",
                "デアル列基本推量形",
            ),
        ),
        (
            Morpheme('決める きめる 決める 動詞 2 * 0 母音動詞 1 基本形 2 "代表表記:決める/きめる 自他動詞:自:決まる/きまる"'),
            (
                "デアル列命令形",
                "デアル列基本形",
                "デアル列基本推量形",
            ),
        ),
        (
            Morpheme('書ける かける 書ける 動詞 2 * 0 母音動詞 1 基本形 2 "代表表記:書ける/かける 可能動詞:書く/かく 補文ト"'),
            (
                "デアル列命令形",
                "デアル列基本形",
                "デアル列基本推量形",
            ),
        ),
    ],
)
def test_call_error_3(m: Morpheme, inf_forms: list[InflectionForm]):
    jinf = Jinf()
    for inf_form in inf_forms:
        with pytest.raises(ValueError):
            _ = jinf(m, inf_form)
