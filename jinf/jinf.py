import json
import os.path
from typing import Dict, Optional

from pyknp import Morpheme

from jinf.inflection_form import InflectionForm, validate_inflection_form
from jinf.inflection_type import InflectionType, validate_inflection_type


class Jinf:
    def __init__(self, dict_path: Optional[str] = None):
        self.dict = self._load_dict(dict_path or self.dict_path)

    def __call__(self, m: Morpheme, target_inf_form: InflectionForm) -> str:
        return self.convert(m.genkei, m.katuyou1, target_inf_form)

    def convert(
        self, lemma: str, inf_type: InflectionType, target_inf_form: InflectionForm
    ):
        if not isinstance(target_inf_form, str) or not validate_inflection_form(
            target_inf_form
        ):
            raise ValueError(f"'{target_inf_form}' is not a valid inflection form")

        if not validate_inflection_type(inf_type):
            raise ValueError(f"'{lemma}' is invariable")

        if target_inf_form not in self.dict[inf_type]:
            raise ValueError(
                f"'{target_inf_form} is not a valid inflection form for '{lemma}'"
            )

        stem = lemma.strip(self.dict[inf_type]["基本形"])
        inf = self.dict[inf_type][target_inf_form]
        return stem if inf == "*" else stem + inf

    @property
    def dict_path(self) -> str:
        return os.path.join(os.path.dirname(__file__), "data", "jinf.json")

    @staticmethod
    def _load_dict(path: str) -> Dict[InflectionType, Dict[InflectionForm, str]]:
        with open(path) as f:
            dat = json.load(f)
        dic = {}
        for inf_type, d in dat.items():
            if inf_type not in dic:
                dic[inf_type] = {}
            for inf_form, inf in d.items():
                dic[inf_type][inf_form] = inf
        return dic
