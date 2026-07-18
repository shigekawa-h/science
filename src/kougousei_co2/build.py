#!/usr/bin/env python3
"""slides/ 内のスライド部品をファイル名順に結合して deck.html を作る。
head.html / tail.html は「build.pyと同じ階層」または「parts/ の中」どちらでも可。
使い方:  python3 build.py  (または python build.py)
"""
from pathlib import Path

root = Path(__file__).parent

def find(name):
    for cand in (root / name, root / "parts" / name):
        if cand.exists():
            return cand.read_text(encoding="utf-8")
    raise FileNotFoundError(f"{name} が見つかりません（同階層 or parts/ に置いてください）")

head = find("head.html")
tail = find("tail.html")
slides = sorted((root / "slides").glob("*.html"))
if not slides:
    raise FileNotFoundError("slides/ に .html がありません")

body = "\n".join(p.read_text(encoding="utf-8").strip() for p in slides)
out = root / "deck.html"
out.write_text(head + "\n" + body + "\n" + tail, encoding="utf-8")
print(f"OK: {out.name} を作成({len(slides)}枚)")
