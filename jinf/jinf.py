import json
import os.path
from typing import Optional, Union

from pyknp import Morpheme

from jinf.inflection_form import InflectionForm
from jinf.inflection_type import InflectionType


class Jinf:
    def __init__(self, dict_path: Optional[str] = None):
        self.dict = self._load_dict(dict_path or self.dict_path)
        import sys

        print(self.dict, file=sys.stderr)

    def __call__(self, m: Morpheme, inf_form: Union[str, InflectionForm]) -> str:
        if isinstance(inf_form, str):
            inf_form = InflectionForm(inf_form)
        if not isinstance(inf_form, InflectionForm):
            raise ValueError(f"'{inf_form}' is not a valid {InflectionForm.__name__}")

        if not InflectionType.has_value(m.katuyou1):
            return m.midasi
        cur_inf_type = InflectionType(m.katuyou1)

        lemma = m.genkei
        stem = lemma.strip(self.dict[cur_inf_type][InflectionForm.KIHON])
        inf = self.dict[cur_inf_type][inf_form]
        if inf == "*":
            return stem
        else:
            return stem + inf

    @property
    def dict_path(self) -> str:
        return os.path.join(os.path.dirname(__file__), "data", "jinf.json")

    @staticmethod
    def _load_dict(path: str) -> dict[InflectionType, dict[InflectionForm, str]]:
        with open(path) as f:
            dat = json.load(f)
        dic = {}
        for inf_type, d in dat.items():
            inf_type = InflectionType(inf_type)
            if inf_type not in dic:
                dic[inf_type] = {}
            for inf_form, inf in d.items():
                inf_form = InflectionForm(inf_form)
                dic[inf_type][inf_form] = inf
        return dic
