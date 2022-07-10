import json
import os.path
from typing import Dict, Optional

from pyknp import Morpheme

from jinf.inflection_form import is_valid_inflection_form
from jinf.inflection_type import is_valid_inflection_type


class Jinf:
    def __init__(self, dict_path: Optional[str] = None):
        self.dict = self._load_dict(dict_path or self.dict_path)

    def __call__(self, m: Morpheme, target_inf_form: str) -> str:
        return self.convert(m.midasi, m.katuyou1, m.katuyou2, target_inf_form)

    def convert(
        self, text: str, inf_type: str, source_inf_form: str, target_inf_form: str
    ):
        if not is_valid_inflection_type(inf_type):
            raise ValueError(f"'{inf_type}' is invariable")

        if not isinstance(source_inf_form, str) or not is_valid_inflection_form(
            source_inf_form
        ):
            raise ValueError(f"'{source_inf_form}' is not a valid inflection form")

        if not isinstance(target_inf_form, str) or not is_valid_inflection_form(
            target_inf_form
        ):
            raise ValueError(f"'{target_inf_form}' is not a valid inflection form")

        if target_inf_form not in self.dict[inf_type]:
            raise ValueError(
                f"'{target_inf_form} is not a valid inflection form for '{text}'"
            )

        stem = text.strip(self.dict[inf_type][source_inf_form])
        inf = self.dict[inf_type][target_inf_form]
        return stem if inf == "*" else stem + inf

    @property
    def dict_path(self) -> str:
        return os.path.join(os.path.dirname(__file__), "data", "jinf.json")

    @staticmethod
    def _load_dict(path: str) -> Dict[str, Dict[str, str]]:
        with open(path) as f:
            dat = json.load(f)
        dic: Dict[str, Dict[str, str]] = {}
        for inf_type, d in dat.items():
            if inf_type not in dic:
                dic[inf_type] = {}
            for inf_form, inf in d.items():
                dic[inf_type][inf_form] = inf
        return dic
