import json
import os.path
from typing import TYPE_CHECKING, Dict

if TYPE_CHECKING:
    from pyknp import Morpheme


class Jinf:
    def __init__(self):
        dict_dir = os.path.join(os.path.dirname(__file__), "data")
        with open(os.path.join(dict_dir, "jinf.json"), "rt") as f:
            self.dict: Dict[str, Dict[str, str]] = json.load(f)
        with open(os.path.join(dict_dir, "e_basic_stem_suffix.json"), "rt") as f:
            self.e_basic_stem_suffix_dict: Dict[str, str] = json.load(f)

    def __call__(
        self, text: str, inf_type: str, source_inf_form: str, target_inf_form: str
    ):
        if not self.is_valid_type(inf_type):
            raise ValueError(f"'{inf_type}' is not a valid inflection type")

        if not self.is_valid_form(inf_type, source_inf_form):
            raise ValueError(
                f"'{source_inf_form}' is not a valid inflection form of '{inf_type}'"
            )

        if not self.is_valid_form(inf_type, target_inf_form):
            raise ValueError(
                f"'{target_inf_form}' is not a valid inflection form of '{inf_type}'"
            )

        if source_inf_form == "エ基本形":
            # TODO: identify the stem
            raise NotImplementedError(f"unable to identify the stem of {text}")
        else:
            stem = text.strip(self.dict[inf_type][source_inf_form])

        if target_inf_form == "エ基本形":
            if stem_suffix := self.e_basic_stem_suffix_dict.get(stem[-1], None):
                stem = stem[:-1] + stem_suffix
            inf = "え"
        else:
            inf = self.dict[inf_type][target_inf_form]

        if inf == "*":
            return stem
        else:
            return stem + inf

    def convert(
        self, text: str, inf_type: str, source_inf_form: str, target_inf_form: str
    ):
        return self(text, inf_type, source_inf_form, target_inf_form)

    def convert_pyknp_morpheme(self, m: "Morpheme", target_inf_form: str) -> str:
        return self(m.genkei, m.katuyou1, "基本形", target_inf_form)

    def is_valid_type(self, inf_type: str) -> bool:
        return inf_type in self.dict

    def is_valid_form(self, inf_type: str, inf_form: str) -> bool:
        return inf_form in self.dict[inf_type]
