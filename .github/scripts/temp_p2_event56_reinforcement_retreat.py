from pathlib import Path

scenario = Path("scenarios/missions/d66_lvl10-16_mission_01_blacksun.md")
s = scenario.read_text(encoding="utf-8")
old = """- 包囲圧力：
  2ラウンド目開始時、  3体以上生存している場合 1d3体追加。
"""
new = """- 包囲圧力：
  2ラウンド目開始時、3体以上生存している場合 1d3体追加する。撤退判定に用いる【初期人数】は戦闘開始時に決定した `1d3+2` 名のままとし、この増援によって初期人数は増加しない。増援は現在人数にのみ加算する。
"""
if s.count(old) != 1:
    raise SystemExit(f"event56 marker count must be 1, got {s.count(old)}")
scenario.write_text(s.replace(old, new, 1), encoding="utf-8")

audit = Path("docs/SCENARIO_V1_01_RESOURCE_BALANCE_AUDIT.md")
a = audit.read_text(encoding="utf-8")
heading = "## 25. Black Sun 出目56の増援と撤退基準 — 承認・反映済み"
section = """

## 25. Black Sun 出目56の増援と撤退基準 — 承認・反映済み

ユーザー承認により、出目56【包囲拡大】の第2ラウンド増援は、Core v1.01の撤退判定に用いる【初期人数】を変更しないものとして明確化する。

- 戦闘開始時の初期人数は `1d3+2` 名。
- 第2ラウンド開始時に3名以上生存している場合、既存どおり `1d3` 名を増援として追加する。
- 増援は現在人数にのみ加算する。
- 撤退判定の基準となる初期人数は、戦闘開始時に決定した `1d3+2` 名のまま固定する。
- 反応が【敵対的】の場合、増援後もこの初期人数の半分以下になった時点でCore v1.01どおり撤退する。

これにより、増援到着によって撤退閾値そのものが後から上昇する解釈を排除し、Coreの【初期人数】の定義を維持する。
"""
if heading not in a:
    audit.write_text(a.rstrip() + section + "\n", encoding="utf-8")
