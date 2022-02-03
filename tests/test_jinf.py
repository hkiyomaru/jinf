import json
import tempfile

import pytest

from jinf import Jinf


def test_init():
    _ = Jinf()


def test_init_error_0():
    with pytest.raises(FileNotFoundError):
        _ = Jinf("foo")


def test_init_error_1():
    with tempfile.NamedTemporaryFile("wt", encoding="utf-8") as f:
        f.write("{")  # invalid json
        with pytest.raises(json.decoder.JSONDecodeError):
            _ = Jinf(f.name)


def test_call_error_0():
    jinf = Jinf()
    with pytest.raises(ValueError):
        jinf(..., "母音動詞_")  # invalid inflection form


def test_call_error_1():
    jinf = Jinf()
    with pytest.raises(ValueError):
        jinf(..., 42)  # invalid inflection form
