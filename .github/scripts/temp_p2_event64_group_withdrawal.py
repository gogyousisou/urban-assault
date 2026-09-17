from pathlib import Path

scenario = Path("scenarios/missions/d66_lvl10-16_mission_01_blacksun.md")
s = scenario.read_text(encoding="utf-8")
old = """- 撤退条件：\n  同行民兵が半数以下（端数切捨て）になった時、反応が【敵対的】であった場合のみ撤退する。\n"""
new = """- 撤退条件：\n  同行民兵が初期人数の半数以下（端数切捨て）になった時、反応が【敵対的】であった場合は、指揮官と生存している同行民兵が一緒に撤退し、その時点で戦闘を終了する。反応が【死ぬまで戦う】の場合、この撤退は発生しない。\n"""
if s.count(old) != 1:
    raise SystemExit(f"Event64 withdrawal anchor count must be 1, got {s.count(old)}")
s = s.replace(old, new, 1)
scenario.write_text(s, encoding="utf-8")

audit = Path("docs/SCENARIO_V1_01_RESOURCE_BALANCE_AUDIT.md")
a = audit.read_text(encoding="utf-8")
heading = "## 48. Black Sun 出目64 同行民兵減少時の撤退主体 — 採用済み"
section = """

## 48. Black Sun 出目64 同行民兵減少時の撤退主体 — 採用済み

ユーザー承認により、出目64【路地裏の指揮官】の撤退条件を満たした場合の撤退主体を明確化する。

- 判定基準は同行民兵の【初期人数】とする。
- 同行民兵が初期人数の半数以下（端数切捨て）になり、反応が【敵対的】である場合、指揮官と生存している同行民兵が一緒に撤退する。
- この撤退が発生した時点で戦闘を終了する。
- 反応が【死ぬまで戦う】の場合、この撤退条件は発生せず、指揮官と同行民兵は戦闘を継続する。
- 指揮官を捕虜にした後の同行民兵については、第47項の規定を適用する。

これにより、高脅威目標である指揮官自身にはCore v1.01の自動撤退を適用せず、出目64に明記されたシナリオ固有の撤退条件によって護衛と一体で撤退する処理を確定する。
"""
if heading not in a:
    a = a.rstrip() + section + "\n"
audit.write_text(a, encoding="utf-8")
