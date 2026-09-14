from pathlib import Path

p = Path("scenarios/missions/d66_lvl10-16_mission_01_blacksun.md")
s = p.read_text(encoding="utf-8")
marker = "- RPG発射：\n"
insert = "- RPG発射：\n  この攻撃は通常の攻撃配分を行わず、必ず分隊長を攻撃対象とする。\n"
if s.count(marker) != 1:
    raise SystemExit(f"target marker count must be 1, got {s.count(marker)}")
p.write_text(s.replace(marker, insert, 1), encoding="utf-8")

a = Path("docs/SCENARIO_V1_01_RESOURCE_BALANCE_AUDIT.md")
t = a.read_text(encoding="utf-8")
heading = "## 19. Black Sun 出目63の攻撃対象 — 採用済み"
section = """

## 19. Black Sun 出目63の攻撃対象 — 採用済み

ユーザー承認により、出目63の特殊攻撃はCore v1.01の通常の攻撃配分を使用せず、分隊長を固定対象とする。

- 奇数ラウンドのみ1回攻撃する既存仕様は変更しない。
- 攻撃対象は必ず分隊長とする。
- 分隊長が通常どおり防御ロールを行う。
- 防御失敗時の既存追加効果は変更しない。

これにより、攻撃回数1を分隊員側へ割り当てることで固有効果を回避できる解釈を排除する。
"""
if heading not in t:
    a.write_text(t.rstrip() + section + "\n", encoding="utf-8")
