from pathlib import Path

scenario = Path("scenarios/missions/d66_lvl10-16_mission_01_blacksun.md")
s = scenario.read_text(encoding="utf-8")
old = """- 指揮統制：\n  指揮官が倒されると、民兵は統率を失い、レベル：4になる。\n"""
new = """- 指揮統制：\n  指揮官が倒される、または【捕虜】になると、民兵は統率を失い、レベル：4になる。指揮官が【捕虜】になった場合、その指揮官は即座に戦闘から除外し、以後は行動・攻撃を行わない。同行民兵が残っている場合、指揮官の捕虜化だけでは戦闘は終了せず、残った民兵との戦闘を継続する。反応が【敵対的】の場合は既存の撤退条件を適用し、【死ぬまで戦う】の場合は同行民兵も通常どおり撤退しない。\n"""
if s.count(old) != 1:
    raise SystemExit(f"Event64 command anchor count must be 1, got {s.count(old)}")
s = s.replace(old, new, 1)
scenario.write_text(s, encoding="utf-8")

audit = Path("docs/SCENARIO_V1_01_RESOURCE_BALANCE_AUDIT.md")
a = audit.read_text(encoding="utf-8")
heading = "## 47. Black Sun 出目64 指揮官捕虜化後の戦闘継続 — 採用済み"
section = """

## 47. Black Sun 出目64 指揮官捕虜化後の戦闘継続 — 採用済み

ユーザー承認により、出目64【路地裏の指揮官】で指揮官を【捕虜】にした場合の同行民兵との戦闘継続を明確化する。

- 指揮官を【捕虜】にした時点で、その指揮官は即座に戦闘から除外し、以後は行動・攻撃を行わない。
- 同行民兵が1体以上残っている場合、指揮官の捕虜化だけでは戦闘は終了しない。
- 残った同行民兵は指揮官を失って統率が低下し、レベル4になる。
- 反応が【敵対的】の場合、同行民兵には既存の撤退条件を適用する。
- 反応が【死ぬまで戦う】の場合、残った同行民兵も撤退せず戦闘を継続する。
- 指揮官を倒した場合の既存のレベル低下も維持する。

これにより、【高脅威目標の捕虜化】と【同行する敵戦闘集団の戦闘終了】を別処理として扱い、Core v1.01の戦闘終了条件との整合を取る。
"""
if heading not in a:
    a = a.rstrip() + section + "\n"
audit.write_text(a, encoding="utf-8")
