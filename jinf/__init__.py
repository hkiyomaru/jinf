from importlib.metadata import version

from jinf.jinf import Jinf

__version__ = version("jinf")

__all__ = [
    "__version__",
    "Jinf",
]
