from importlib.metadata import version

from jinf.inflection_form import INFECTION_FORMS, InflectionForm
from jinf.inflection_type import INFLECTION_TYPES, InflectionType
from jinf.jinf import Jinf

__version__ = version("jinf")

__all__ = [
    "__version__",
    "Jinf",
    "INFECTION_FORMS",
    "InflectionForm",
    "INFLECTION_TYPES",
    "InflectionType",
]
