from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected 1 match, found {count}")
    return text.replace(old, new, 1)


core_path = Path("core/core-rule-full.md")
text = core_path.read_text(encoding="utf-8")

text = replace_once(
    text,
    ">射撃回数：2回  \n>【攻撃ロール】に ＋1 の修正を与えます。但し弾倉を追加で1消費します。  ",
    ">射撃回数：2回  \n>【攻撃ロール】に ＋1 の修正を与えます。  \n>2回とも射撃する場合、弾倉は合計2個消費します。  ",
    "LMG ammo wording",
)

text = replace_once(
    text,
    ">各攻撃ごとに弾倉を追加で1消費します（1ラウンド合計2消費）。  ",
    ">2回とも射撃する場合、弾倉は合計2個消費します。  ",
    "Gunner ammo wording",
)

core_path.write_text(text, encoding="utf-8")

p0_path = Path("docs/CORE_V1_01_P0_DECISIONS.md")
p0 = p0_path.read_text(encoding="utf-8")
marker = "- 常備装備・消耗装備の取得コストは軍票に統一。"
replacement = marker + "\n- LMG／ガンナーの弾倉表記を、承認済みの『射撃回数2なら原則合計2個消費』に合わせて明確化。"
if p0.count(marker) != 1:
    raise SystemExit(f"P0 marker: expected 1 match, found {p0.count(marker)}")
p0 = p0.replace(marker, replacement, 1)
p0_path.write_text(p0, encoding="utf-8")
