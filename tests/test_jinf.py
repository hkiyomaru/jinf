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
