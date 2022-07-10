from importlib.metadata import version

from jinf.inflection_form import INFLECTION_FORMS
from jinf.inflection_type import INFLECTION_TYPES
from jinf.jinf import Jinf

__version__ = version("jinf")

__all__ = [
    "__version__",
    "Jinf",
    "INFLECTION_FORMS",
    "INFLECTION_TYPES",
]
