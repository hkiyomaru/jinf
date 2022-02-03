import pytest

from jinf import InflectionType
from jinf.inflection_type import validate_inflection_type


@pytest.mark.parametrize(
    "inf_type",
    [
        "母音動詞",
        "子音動詞カ行",
        "子音動詞カ行促音便形",
        "子音動詞ガ行",
        "子音動詞サ行",
        "子音動詞タ行",
        "子音動詞ナ行",
        "子音動詞バ行",
        "子音動詞マ行",
        "子音動詞ラ行",
        "子音動詞ラ行イ形",
        "子音動詞ワ行",
        "子音動詞ワ行文語音便形",
        "カ変動詞",
        "カ変動詞来",
        "サ変動詞",
        "ザ変動詞",
        "イ形容詞アウオ段",
        "イ形容詞イ段",
        "イ形容詞イ段特殊",
        "ナ形容詞",
        "ナノ形容詞",
        "ナ形容詞特殊",
        "タル形容詞",
        "判定詞",
        "無活用型",
        "助動詞ぬ型",
        "助動詞だろう型",
        "助動詞そうだ型",
        "助動詞く型",
        "動詞性接尾辞ます型",
        "動詞性接尾辞うる型",
    ],
)
def test_inflection_type(inf_type: InflectionType):
    assert validate_inflection_type(inf_type) is True


def test_inflection_type_error():
    assert validate_inflection_type("foo") is False
