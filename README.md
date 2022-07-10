# Jinf: Japanese Inflection Converter

[![test](https://github.com/hkiyomaru/jinf/actions/workflows/test.yml/badge.svg)](https://github.com/hkiyomaru/jinf/actions/workflows/test.yml)

**Jinf** is a Japanese inflection converter.
Jinf depends on [JumanDic](https://github.com/ku-nlp/JumanDIC) and follows the grammar.

## Installation

```shell
pip install jinf
```

## Usage

```python
from jinf import Jinf

jinf = Jinf()

text = "走る"
inf_type = "子音動詞ラ行"
source_inf_form = "基本形"
print(jinf(text, inf_type, source_inf_form, "基本形"))  # 走る
print(jinf(text, inf_type, source_inf_form, "未然形"))  # 走ら
print(jinf(text, inf_type, source_inf_form, "意志形"))  # 走ろう
print(jinf(text, inf_type, source_inf_form, "命令形"))  # 走れ
print(jinf(text, inf_type, source_inf_form, "三角形"))  # ValueError: '三角形' is not a valid inflection form
print(jinf(text, inf_type, source_inf_form, "デアル列命令形"))  # ValueError: 'デアル列命令形' is not a valid inflection form of '子音動詞ラ行'
```

### [pyknp](https://github.com/ku-nlp/pyknp) integration

[pyknp](https://github.com/ku-nlp/pyknp) is the official Python binding for Jumanpp.
To enable the pyknp integration, specify the extra requirement when installing Jinf:

```shell
pip install jinf[pyknp]
```

[Morpheme](https://pyknp.readthedocs.io/en/latest/mrph.html#module-pyknp.juman.morpheme) objects can be used as input for Jinf as follows.

```python
from jinf import Jinf
from pyknp import Morpheme

jinf = Jinf()

mrph = Morpheme('走る はしる 走る 動詞 2 * 0 子音動詞ラ行 10 基本形 2 "代表表記:走る/はしる"')
print(jinf.convert_pyknp_morpheme(mrph, "基本形"))  # 走る
print(jinf.convert_pyknp_morpheme(mrph, "未然形"))  # 走ら
print(jinf.convert_pyknp_morpheme(mrph, "意志形"))  # 走ろう
print(jinf.convert_pyknp_morpheme(mrph, "命令形"))  # 走れ
print(jinf.convert_pyknp_morpheme(mrph, "三角形"))  # ValueError: '三角形' is not a valid inflection form
print(jinf.convert_pyknp_morpheme(mrph, "デアル列命令形"))  # ValueError: 'デアル列命令形' is not a valid inflection form of '子音動詞ラ行'
```

## List of available inflection types/forms

Run the following:

```python
from jinf import INFLECTION_TYPES, INFLECTION_FORMS

print(INFLECTION_TYPES)  # ["母音動詞", "子音動詞カ行", "子音動詞カ行促音便形", ...]
print(INFLECTION_FORMS)  # ["語幹", "基本形", "未然形", ...]
```

See [JUMAN.katuyou](https://github.com/ku-nlp/JumanDIC/blob/master/grammar/JUMAN.katuyou) in [JumanDic](https://github.com/ku-nlp/JumanDIC) for details.
