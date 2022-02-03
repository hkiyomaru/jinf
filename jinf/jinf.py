import json
import os.path
from logging import getLogger
from typing import Optional

from pyknp import Morpheme

from jinf.inflection_form import InflectionForm, validate_inflection_form
from jinf.inflection_type import InflectionType, validate_inflection_type

logger = getLogger(__file__)


class Jinf:
    def __init__(self, dict_path: Optional[str] = None):
        self.dict = self._load_dict(dict_path or self.dict_path)

    def __call__(self, m: Morpheme, inf_form: InflectionForm) -> str:
        if not isinstance(inf_form, str) or not validate_inflection_form(inf_form):
            raise ValueError(f"'{inf_form}' is not a valid inflection form")

        cur_inf_type = m.katuyou1
        if not validate_inflection_type(cur_inf_type):
            raise ValueError(
                f"'{inf_form} is not a valid inflection form for '{m.midasi}'"
            )
        if inf_form not in self.dict[cur_inf_type]:
            raise ValueError(
                f"'{inf_form} is not a valid inflection form for '{m.midasi}'"
            )

        lemma = m.genkei
        stem = lemma.strip(self.dict[cur_inf_type]["基本形"])
        inf = self.dict[cur_inf_type][inf_form]
        return stem if inf == "*" else stem + inf

    @property
    def dict_path(self) -> str:
        return os.path.join(os.path.dirname(__file__), "data", "jinf.json")

    @staticmethod
    def _load_dict(path: str) -> dict[InflectionType, dict[InflectionForm, str]]:
        with open(path) as f:
            dat = json.load(f)
        dic = {}
        for inf_type, d in dat.items():
            if inf_type not in dic:
                dic[inf_type] = {}
            for inf_form, inf in d.items():
                dic[inf_type][inf_form] = inf
        return dic
