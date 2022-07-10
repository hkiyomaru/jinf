# Jinf: Japanese Inflection Converter

[![test](https://img.shields.io/github/workflow/status/hkiyomaru/jinf/test?label=test&logo=Github&style=flat-square)](https://github.com/hkiyomaru/jinf/actions/workflows/test.yml)
![PyPI](https://img.shields.io/pypi/v/jinf?style=flat-square)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/jinf?style=flat-square)
![License - MIT](https://img.shields.io/github/license/hkiyomaru/jinf?style=flat-square)

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
print(jinf(text, inf_type, source_inf_form, "三角形"))  # ValueError: '三角形' is not a valid inflection form of '子音動詞ラ行'
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
print(jinf.convert_pyknp_morpheme(mrph, "三角形"))  # ValueError: '三角形' is not a valid inflection form of '子音動詞ラ行'
print(jinf.convert_pyknp_morpheme(mrph, "デアル列命令形"))  # ValueError: 'デアル列命令形' is not a valid inflection form of '子音動詞ラ行'
```

## List of available inflection types/forms

See [JUMAN.katuyou](https://github.com/ku-nlp/JumanDIC/blob/master/grammar/JUMAN.katuyou) in [JumanDic](https://github.com/ku-nlp/JumanDIC).
