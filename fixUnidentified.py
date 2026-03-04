#!/usr/bin/env python3
"""
fixUnidentified.py — Replaces "Unidentified" item names in items.txt using a reference server as source.

For each item in the source items.txt that contains "Unidentified" in the name,
looks up the same ID in the reference items.txt and replaces the name if the
reference has a proper name.

Usage:
    python fixUnidentified.py
    python fixUnidentified.py --source items_laRO.txt --reference items_iRO.txt --output items.txt
"""

import argparse
from pathlib import Path


def load_items(path: Path) -> dict[int, str]:
    items = {}
    for line in path.read_text(encoding='utf-8').splitlines():
        line = line.strip()
        if not line:
            continue
        parts = line.split('#')
        if len(parts) >= 2 and parts[0].isdigit():
            items[int(parts[0])] = parts[1]
    return items


def parse_args():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('--source',    '-s', default='items_source.txt',    type=Path, help='Your server items.txt (input)')
    p.add_argument('--reference', '-r', default='items_reference.txt', type=Path, help='Reference items.txt (e.g. iRO)')
    p.add_argument('--output',    '-o', default='items.txt',           type=Path, help='Fixed output file')
    return p.parse_args()


def main():
    args = parse_args()

    source    = load_items(args.source)
    reference = load_items(args.reference)

    fixed     = 0
    not_found = 0
    also_unid = 0

    result = {}
    for item_id, name in source.items():
        if 'Unidentified' not in name:
            result[item_id] = name
            continue

        ref_name = reference.get(item_id)

        if ref_name is None:
            not_found += 1
            result[item_id] = name
        elif 'Unidentified' in ref_name:
            also_unid += 1
            result[item_id] = name
        else:
            fixed += 1
            result[item_id] = ref_name

    lines = [f"{item_id}#{name}#" for item_id, name in result.items()]
    args.output.write_text('\n'.join(lines) + '\n', encoding='utf-8')

    print(f"✓ Fixed:                       {fixed}")
    print(f"✗ Not in reference:            {not_found}")
    print(f"✗ Also Unidentified in reference: {also_unid}")
    print(f"→ Output: {args.output}")


if __name__ == '__main__':
    main()