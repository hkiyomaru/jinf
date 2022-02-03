# jinf: Japanese Inflection Converter

**jinf** is a Japanese inflection converter.

## Usage

```python
import pyknp  # A Python Binding for Juman++

from jinf import Jinf

juman = pyknp.Juman()
jinf = Jinf()

text = "走る"
analysis = juman.analysis(text)

for mrph in analysis.mrph_list():
    print(mrph.midasi)
    for inf_ty in ("基本形", "未然形", "意志形"):
        print(f" - {inf_ty}: {jinf(mrph, inf_ty)}")
    print("---")
```
