#!/usr/bin/env python3
"""Convert bibliography/publications.bib into Jekyll _data YAML.

Edit only the BibTeX file. The site deployment runs this script before Jekyll.
Custom BibTeX fields: category (P/C/W/J), venue, number, paper, code, poster.
"""
from pathlib import Path
import argparse
import re
import bibtexparser
import yaml

ROOT = Path(__file__).resolve().parent.parent


def normalize_authors(raw):
    # Standard BibTeX separates authors with 'and'. Legacy records can use
    # display-ready comma-separated names; preserve those verbatim.
    if re.search(r"\s+and\s+", raw, flags=re.I):
        return ", ".join(re.split(r"\s+and\s+", raw, flags=re.I))
    return raw


def infer_category(entry):
    if entry.get("category"):
        return entry["category"].upper().strip()
    journal = entry.get("journal", "").lower()
    if any(term in journal for term in ("arxiv", "preprint", "under review")):
        return "P"
    if entry.get("booktitle"):
        return "C"
    if entry.get("journal"):
        return "J"
    return "P"


def infer_venue(entry, category):
    return entry.get("venue") or entry.get("journal") or entry.get("booktitle") or (
        "Preprint / under review" if category == "P" else "Publication"
    )


def infer_link(entry):
    if entry.get("paper") or entry.get("url"):
        return entry.get("paper") or entry.get("url")
    if entry.get("eprint") and (
        entry.get("archiveprefix", "").lower() == "arxiv" or
        re.fullmatch(r"[0-9]{4}\\.[0-9]{4,5}", entry["eprint"])
    ):
        return "https://arxiv.org/abs/" + entry["eprint"]
    if entry.get("doi"):
        return "https://doi.org/" + entry["doi"]
    return None


def convert(source, target_dir, check=False):
    with source.open(encoding="utf-8") as handle:
        entries = bibtexparser.load(handle).entries
    if not entries:
        raise ValueError("BibTeX file contains no publications")

    seen_ids = set()
    records = []
    for entry in entries:
        entry_id = entry.get("ID", "")
        if entry_id in seen_ids:
            raise ValueError(f"Duplicate BibTeX entry key: {entry_id}")
        seen_ids.add(entry_id)
        category = infer_category(entry)
        if category not in {"P", "C", "W", "J"}:
            raise ValueError(f"{entry_id}: category must be P, C, W or J")
        for required in ("title", "author", "year"):
            if not entry.get(required):
                raise ValueError(f"{entry_id}: missing {required}")
        item = {
            "year": int(entry["year"]),
            "title": entry["title"].strip(),
            "authors": normalize_authors(entry["author"].strip()),
            "venue": infer_venue(entry, category),
            "category": category,
        }
        for optional in ("paper", "code", "poster", "number"):
            if entry.get(optional):
                item[optional] = entry[optional].strip()
        link = infer_link(entry)
        if link:
            item["paper"] = link.strip()
        records.append(item)
    seen_numbers = set()
    for c in ("P", "C", "W", "J"):
        group = [e for e in records if e["category"] == c]
        # Preserve existing numbering; allocate numbers for newly pasted entries.
        used = {e["number"] for e in group if "number" in e}
        counter = max([int(n[1:]) for n in used if re.fullmatch(rf"{c}[0-9]+", n)] or [0])
        for e in group:
            if "number" not in e:
                counter += 1
                e["number"] = f"{c}{counter}"
            if e["number"] in seen_numbers:
                raise ValueError(f"Duplicate publication number: {e['number']}")
            seen_numbers.add(e["number"])
    preprints = sorted((e for e in records if e["category"] == "P"), key=lambda e: (-e["year"], -int(e["number"][1:])))
    papers = sorted((e for e in records if e["category"] != "P"), key=lambda e: (-e["year"], e["category"], -int(e["number"][1:])))
    target_dir.mkdir(parents=True, exist_ok=True)
    for name, data in (("preprints.yml", preprints), ("papers.yml", papers)):
        dest = target_dir / name
        output = yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=150)
        if check:
            if not dest.exists() or dest.read_text(encoding="utf-8") != output:
                print(f"{dest}: generation needed")
        else:
            dest.write_text(output, encoding="utf-8")
            print(f"Wrote {dest}: {len(data)} records")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    convert(ROOT / "bibliography" / "publications.bib", ROOT / "_data", args.check)
