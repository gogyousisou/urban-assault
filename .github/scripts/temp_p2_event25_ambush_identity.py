from pathlib import Path

scenario = Path("scenarios/missions/d66_lvl10-16_mission_01_blacksun.md")
s = scenario.read_text(encoding="utf-8")
old = "    罠だった。周囲に潜んでいた民兵が発砲する。敵が先制攻撃を行う。"
new = "    罠だった。近づいてきた民兵たちが一斉に発砲する。敵が先制攻撃を行う。"
if s.count(old) != 1:
    raise SystemExit(f"event25 hostile text count must be 1, got {s.count(old)}")
scenario.write_text(s.replace(old, new, 1), encoding="utf-8")

audit = Path("docs/SCENARIO_V1_01_RESOURCE_BALANCE_AUDIT.md")
a = audit.read_text(encoding="utf-8")
heading = "## 42. Black Sun 出目25の敵対時戦闘主体 — 採用済み"
section = """

## 42. Black Sun 出目25の敵対時戦闘主体 — 採用済み

ユーザー承認により、出目25【離反した民兵】が敵対した場合に戦闘するのは、別途未定義の伏兵ではなく、出現数として定義されている民兵1d2名自身とする。

- 敵対時の文章を「罠だった。近づいてきた民兵たちが一斉に発砲する。敵が先制攻撃を行う。」へ変更する。
- 敵数は現行どおり民兵1d2名とする。
- レベル4、戦利品：なしは変更しない。
- 追加の伏兵・民兵は出現しない。

これにより、本文上の戦闘主体と出現数・レベルの定義を一致させ、未定義の追加敵が発生する解釈を排除する。
"""
if heading not in a:
    audit.write_text(a.rstrip() + section + "\n", encoding="utf-8")
