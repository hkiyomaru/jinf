"""This script parses `JUMAN.katuyou` and creates `jinf.json`.

Usage:
    python3 parse_jumandic.py <path-to-jinf.json>
"""
import argparse
import json

parser = argparse.ArgumentParser("List inflection types in jinf.json.")
parser.add_argument("IN", help="Path to jinf.json.")
args = parser.parse_args()

with open(args.IN) as f:
    dic = json.load(f)

inf_types = []
for v in dic.values():
    for k in v.keys():
        if k not in inf_types:
            inf_types.append(k)

print("\n".join(inf_types))
