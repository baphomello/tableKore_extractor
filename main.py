#!/usr/bin/env python3
"""
main.py — Generates OpenKore table files from iteminfo.lub

Usage:
    python main.py --items
    python main.py --descriptions
    python main.py --items --descriptions
    python main.py --items --input "C:/Ragnarok/System/iteminfo.lub"

Flags:
    --input  / -i   Path to iteminfo.lub  (default: C:/Ragnarok/System/iteminfo.lub)
    --items  / -n   Generate items.txt
    --descriptions / -d   Generate itemsdescriptions.txt
"""

import argparse
from pathlib import Path

from parser  import ItemInfoParser
from writers import write_items, write_descriptions, write_slot_count

DEFAULT_INPUT = Path('C:/Ragnarok/System/iteminfo.lub')


def parse_args():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('--input',        '-i', type=Path, default=Path('iteminfo.lub'))
    p.add_argument('--items',        '-n', action='store_true', help='Generate items.txt')
    p.add_argument('--descriptions', '-d', action='store_true', help='Generate itemsdescriptions.txt')
    p.add_argument('--slots',        '-s', action='store_true', help='Generate itemslotcounttable.txt')
    return p.parse_args()


def resolve_input(path: Path) -> Path:
    if path.exists():
        return path
    if DEFAULT_INPUT.exists():
        print(f"Using default: {DEFAULT_INPUT}")
        return DEFAULT_INPUT
    raise FileNotFoundError(f"File not found: {path}\nUse --input to specify the correct path.")


def main():
    args = parse_args()

    if not any([args.items, args.descriptions, args.slots]):
        print("Nothing to do. Use --items, --descriptions, --slots, or any combination.")
        return

    items = ItemInfoParser(resolve_input(args.input)).parse()
    print(f"Parsed {len(items)} items from {args.input.name}")

    if args.items:
        write_items(items, 'items.txt')

    if args.descriptions:
        write_descriptions(items, 'itemsdescriptions.txt')

    if args.slots:
        write_slot_count(items, 'itemslotcounttable.txt')


if __name__ == '__main__':
    main()