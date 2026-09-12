from pathlib import Path

path = Path("scenarios/missions/d66_lvl12-16_mission_01_blacksun.md")
text = path.read_text(encoding="utf-8")
replacements = [
    ("## 10. プロローグ", "## 11. プロローグ"),
    ("## 11. マップ表(d66)", "## 12. マップ表(d66)"),
    ("## 12. 中間イベント", "## 13. 中間イベント"),
    ("## 13.最終イベント", "## 14. 最終イベント"),
    ("## 14. エピローグ", "## 15. エピローグ"),
]
for old, new in replacements:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"expected one match for {old!r}, found {count}")
    text = text.replace(old, new, 1)
path.write_text(text, encoding="utf-8")
