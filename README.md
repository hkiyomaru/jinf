# Jinf: Japanese Inflection Converter

**Jinf** is a Japanese inflection converter.
Jinf depends on [JumanDic](https://github.com/ku-nlp/JumanDIC) and follows the grammar.

## Installation

```shell
pip install jinf
```

## Usage

### [pyknp](https://github.com/ku-nlp/pyknp) integration

[pyknp](https://github.com/ku-nlp/pyknp) is the official Python binding for Jumanpp.
Instances of [the Morpheme class](https://pyknp.readthedocs.io/en/latest/mrph.html#module-pyknp.juman.morpheme) can be used as input for Jinf.

```python
from jinf import Jinf
from pyknp import Morpheme

jinf = Jinf()

mrph = Morpheme('走る はしる 走る 動詞 2 * 0 子音動詞ラ行 10 基本形 2 "代表表記:走る/はしる"')

print(mrph.midasi)          # 走る
print(mrph.genkei)          # 走る

print(jinf(mrph, "基本形"))  # 走る
print(jinf(mrph, "未然形"))  # 走ら
print(jinf(mrph, "意志形"))  # 走ろう
print(jinf(mrph, "命令形"))  # 走れ

mrph = Morpheme('言語 げんご 言語 名詞 6 普通名詞 1 * 0 * 0 "代表表記:言語/げんご カテゴリ:抽象物"')
print(jinf(mrph, "基本形"))  # ValueError: '言語' is invariable

mrph = Morpheme('走る はしる 走る 動詞 2 * 0 子音動詞ラ行 10 基本形 2 "代表表記:走る/はしる"')
print(jinf(mrph, "三角形"))  # ValueError: '三角形' is not a valid inflection form

mrph = Morpheme('走る はしる 走る 動詞 2 * 0 子音動詞ラ行 10 基本形 2 "代表表記:走る/はしる"')
print(jinf(mrph, "デアル列命令形"))  # ValueError: 'デアル列命令形' is not a valid inflection form for '走る'
```

### Manual

Jinf also can be used by manually providing linguistic information.

```python
from jinf import Jinf

jinf = Jinf()

lemma = "走る"            # corresponds to `mrph.genkei` in pyknp
inf_type = "子音動詞ラ行"  # corresponds to `mrph.katuyou1` in pyknp

print(jinf.convert(lemma, inf_type, "基本形"))  # 走る
print(jinf.convert(lemma, inf_type, "未然形"))  # 走ら
print(jinf.convert(lemma, inf_type, "意志形"))  # 走ろう
print(jinf.convert(lemma, inf_type, "命令形"))  # 走れ
```

## List of available inflection types/forms

Run the following:

```python
from jinf import INFLECTION_TYPES, INFLECTION_FORMS

print(INFLECTION_TYPES)  # ["母音動詞", "子音動詞カ行", "子音動詞カ行促音便形", ...]
print(INFLECTION_FORMS)  # ["語幹", "基本形", "未然形", ...]
```

See [JUMAN.katuyou](https://github.com/ku-nlp/JumanDIC/blob/master/grammar/JUMAN.katuyou) in [JumanDic](https://github.com/ku-nlp/JumanDIC).
