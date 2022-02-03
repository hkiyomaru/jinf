# Jinf: Japanese Inflection Converter

**Jinf** is a Japanese inflection converter.
Jinf depends on [JumanDic](https://github.com/ku-nlp/JumanDIC) and follows the grammar.

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
```
