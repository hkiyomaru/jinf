import pytest

from jinf import InflectionForm


@pytest.mark.parametrize("ty", ["語幹", "基本形", "未然形", "意志形"])
def test_inflection_form(ty: str):
    assert InflectionForm(ty).name


def test_inflection_form_error():
    with pytest.raises(ValueError):
        _ = InflectionForm("foo")
