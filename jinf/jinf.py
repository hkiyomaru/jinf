import json
import os.path
from typing import Optional, Union

from pyknp import Morpheme

from jinf.inflection_form import InflectionForm
from jinf.inflection_type import InflectionType


class Jinf:
    def __init__(self, dict_path: Optional[str] = None):
        self.dict = self._load_dict(dict_path or self.dict_path)

    def __call__(self, m: Morpheme, inf_form: Union[str, InflectionForm]) -> str:
        pass

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
