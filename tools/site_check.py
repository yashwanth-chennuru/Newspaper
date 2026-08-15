#!/usr/bin/env python3
"""Minimal static-site checks; uses only the Python standard library."""
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import sys

ROOT = Path(__file__).resolve().parents[1]


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: list[str] = []
        self.links: list[str] = []
        self.external_scripts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id"):
            self.ids.append(values["id"])
        if tag == "a" and values.get("href"):
            self.links.append(values["href"])
        if tag == "script" and values.get("src"):
            self.external_scripts.append(values["src"])


def is_local_link(href: str) -> bool:
    parts = urlsplit(href)
    return not parts.scheme and not parts.netloc and not href.startswith(("#", "mailto:"))


def check_page(page: Path) -> list[str]:
    parser = PageParser()
    parser.feed(page.read_text(encoding="utf-8"))
    errors: list[str] = []
    duplicates = sorted({item for item in parser.ids if parser.ids.count(item) > 1})
    if duplicates:
        errors.append(f"{page.relative_to(ROOT)}: duplicate IDs: {', '.join(duplicates)}")
    if parser.external_scripts:
        errors.append(f"{page.relative_to(ROOT)}: external scripts are not allowed: {', '.join(parser.external_scripts)}")
    for href in parser.links:
        if is_local_link(href):
            target = page.parent / urlsplit(href).path
            if not target.resolve().exists():
                errors.append(f"{page.relative_to(ROOT)}: broken local link: {href}")
    return errors


def main() -> int:
    errors = [error for page in ROOT.rglob("*.html") for error in check_page(page)]
    if errors:
        print("Static-site checks failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    pages = len(list(ROOT.rglob("*.html")))
    print(f"Static-site checks passed ({pages} HTML pages checked).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
