import pytest

from jinf import InflectionType


@pytest.mark.parametrize("ty", ["母音動詞", "子音動詞カ行"])
def test_inflection_type(ty: str):
    assert InflectionType(ty).name


def test_inflection_type_error():
    with pytest.raises(ValueError):
        _ = InflectionType("foo")
