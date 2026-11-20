#!/usr/bin/env python3
"""Regenerate the icon tables in ranger/gui/icons.py from yazi's theme-dark.toml.

Usage: sync_yazi_icons.py [PATH_OR_URL]
Default source: yazi's preset theme-dark.toml on GitHub (main).
"""
import os
import re
import sys
import tomllib
import urllib.request

URL = "https://raw.githubusercontent.com/sxyazi/yazi/main/yazi-config/preset/theme-dark.toml"
ICONS = os.path.join(os.path.dirname(__file__), "..", "..", "ranger", "gui", "icons.py")


def esc(text):
    return "".join(
        c if ord(c) < 0x80 else
        ("\\u%04x" % ord(c) if ord(c) < 0x10000 else "\\U%08x" % ord(c))
        for c in text)


def table(name, comment, entries):
    out = ["# " + "-" * 75, "# " + comment, "# " + "-" * 75, name + " = {"]
    seen = set()
    for entry in entries:
        key = entry["name"].lower()
        if key not in seen:
            seen.add(key)
            out.append("    %r: '%s'," % (key, esc(entry["text"])))
    out.append("}")
    return out


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else URL
    if src.startswith("http"):
        raw = urllib.request.urlopen(src).read()
    else:
        raw = open(src, "rb").read()
    icon = tomllib.loads(raw.decode())["icon"]
    cond = {c["if"]: c["text"] for c in icon["conds"]}
    lines = [
        "# " + "-" * 75,
        "# Default / fallback icons (yazi [icon].conds)",
        "# " + "-" * 75,
        "ICON_DIRECTORY = '%s'" % esc(cond["dir"]),
        "ICON_DIRECTORY_LINK = '%s'" % esc(cond["link"]),
        "ICON_FILE = '%s'" % esc(cond["!dir"]),
        "ICON_FILE_LINK = '%s'" % esc(cond["link"]),
        "ICON_LINK_BAD = '%s'" % esc(cond["orphan"]),
        "ICON_EXEC = '%s'" % esc(cond["exec"]),
        "ICON_FIFO = '%s'" % esc(cond["fifo"]),
        "ICON_SOCKET = '%s'" % esc(cond["sock"]),
        "ICON_BLOCK = '%s'" % esc(cond["block"]),
        "",
        "# Separator appended after the icon (yazi: one space)",
        "ICON_SEPARATOR = ' '",
        "",
    ]
    lines += table("ICONS_BY_DIRNAME", "Icons by directory name  (lowercase basename -> glyph)", icon["dirs"]) + [""]
    lines += table("ICONS_BY_FILENAME", "Icons by exact filename  (lowercase -> glyph)", icon["files"]) + [""]
    lines += table("ICONS_BY_EXTENSION", "Icons by file extension  (lowercase -> glyph)", icon["exts"]) + ["", ""]

    path = os.path.normpath(ICONS)
    text = open(path, encoding="utf-8").read().split("\n")
    start = next(i for i, l in enumerate(text) if l.startswith("# Default / fallback")) - 1
    end = next(i for i, l in enumerate(text) if l.startswith("def get_icon"))
    open(path, "w", encoding="utf-8").write("\n".join(text[:start] + lines + text[end:]))


if __name__ == "__main__":
    main()
