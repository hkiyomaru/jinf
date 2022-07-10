"""This script parses `JUMAN.katuyou` and creates `jinf.json`.

Note:
    `JUMAN.katuyou` can be found at https://github.com/ku-nlp/JumanDIC.

Usage:
    python3 parse_jumandic.py <path-to-JUMAN.katuyou> <path-to-dir-to-save-jinf.json>
"""
import argparse
import json
import os
from typing import Dict, Optional

parser = argparse.ArgumentParser("Parse JUMAN.katuyou and create jinf.json.")
parser.add_argument("IN", help="Path to JUMAN.katuyou.")
parser.add_argument("OUT", help="Path to the directory to save jinf.json.")
args = parser.parse_args()

dic = ""
with open(args.IN) as f:
    for line in f:
        if line.strip() == "":
            continue
        if ";" in line:
            dic += line[: line.index(";")]
        else:
            dic += line

p = 0
level = 0

inf_form: Optional[str] = None
inf_type: Optional[str] = None
inf: Optional[str] = None

jinf: Dict[str, Dict[str, str]] = {}

while True:
    # EOF: break
    if p == len(dic) - 1:
        break

    # Read the current character and advance the pointer.
    c = dic[p]
    p += 1

    # Skip the character if it is an empty.
    if c.strip() == "":
        continue

    if c == "(":
        level += 1
        if level == 1:
            pp = p
            while dic[pp] != "(":
                pp += 1
            inf_type = dic[p:pp].strip()
            if inf_type not in jinf:
                jinf[inf_type] = {}
            p = pp
        elif level == 2:
            pass
        elif level == 3:
            pp = p
            while dic[pp].strip() != "":
                pp += 1
            inf_form = dic[p:pp].strip()
            p = pp

            while dic[p].strip() == "":
                p += 1

            pp = p
            while dic[pp].strip() != ")":
                pp += 1
            if inf_type == "カ変動詞来":
                inf = dic[p:pp].split()[0].strip()
            else:
                inf = dic[p:pp].strip()
            p = pp

            assert isinstance(inf_type, str)
            assert isinstance(inf_form, str)
            assert isinstance(inf, str)
            jinf[inf_type][inf_form] = inf
    if c == ")":
        level -= 1

with open(os.path.join(args.OUT, "jinf.json"), "wt") as f:
    json.dump(jinf, f, ensure_ascii=False, indent=4)
