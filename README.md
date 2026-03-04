# Openkore Items Extractor

> Generate [OpenKore](https://github.com/OpenKore/openkore) table files directly from your Ragnarok Online client — always in sync, never outdated.

---

Ragnarok Online servers constantly add new items, update names, and expand their item pool. Maintaining `items.txt` and `itemsdescriptions.txt` by hand is tedious and error-prone. **Openkore Items Extractor** automates this entirely: it reads `iteminfo.lub` straight from your RO client and generates ready-to-use OpenKore table files in seconds.

No more copy-pasting. No more "Unknown Item (12345)". Every update, just run one command.

---

## What it generates

| File                    | Description                                       |
| ----------------------- | ------------------------------------------------- |
| `items.txt`             | Item IDs and display names in OpenKore format     |
| `itemsdescriptions.txt` | Full item descriptions, clean and color-code-free |

---

## Requirements

- Python 3.10+
- `iteminfo.lub` from your RO client's GRF or `System/` folder

---

## Usage

```bash
# Generate both files at once (recommended)
python main.py --items --descriptions

# Generate only items.txt
python main.py --items

# Generate only itemsdescriptions.txt
python main.py --descriptions

# Specify a custom path to iteminfo.lub
python main.py --items --descriptions --input "C:/Ragnarok/System/iteminfo.lub"
```

The generated files will appear in the same directory. Copy them to your OpenKore `tables/<server>/` folder.

---

## How it works

RO clients store item data in a Lua file called `iteminfo.lub` inside GRF file or in the `System/` folder. This file contains the names and descriptions that the **client itself uses** — meaning it's always accurate, always up to date, and always in the language your server runs.

**Openkore Items Extractor** parses this file, extracts the `identifiedDisplayName` and `identifiedDescriptionName` for each item, strips RO color codes (like `^0000FF` and `^000000`) from descriptions, and writes clean output files ready to drop into OpenKore.

```
iteminfo.lub  →  parser.py  →  writers.py  →  items.txt
                                           →  itemsdescriptions.txt
```

---

## Project structure

```
iteminfo-tools/
├── main.py      # CLI entry point — run this
├── parser.py    # Reads iteminfo.lub, returns Item dataclasses
└── writers.py   # Writes items.txt and itemsdescriptions.txt
```

Each file has a single responsibility and can be imported independently if you want to integrate the parser into a larger project.

---

## After a server update

1. Open GRF Editor (or your preferred extractor)
2. Locate `System/iteminfo.lub` in your client folder
3. Run `python main.py --items --descriptions`
4. Copy the output files to `tables/<server>/` in your OpenKore installation

That's it.

---

## Contributing

Contributions are welcome! Some ideas if you want to help:

- **Support for other servers** — the parser works with any server that uses the standard `iteminfo.lub` format. If yours uses a different structure, open an issue with a sample and we'll add support.
- **Monster and map table generators** — the same approach applies to `monsterinfo.lub`, `accessoryid.lub`, and others.
- **Output format options** — some OpenKore forks use slightly different table formats.
- **Tests** — unit tests for the parser and writers would be a great addition.

To contribute, fork the repo, make your changes, and open a pull request. Keep the code clean, single-responsibility, and consistent with the existing style.

---

## License

[MIT](LICENSE) — do whatever you want with it.
