from pathlib import Path

scenario = Path("scenarios/missions/d66_lvl10-16_mission_01_blacksun.md")
s = scenario.read_text(encoding="utf-8")
old = "戦闘する場合は先制攻撃ができる。"
new = "中立を確認した後で戦闘を開始する場合、敵の反応を【敵対的】として扱い、分隊側が先攻となる。この先攻は行動順だけを変更し、Core v1.01の遭遇時選択【先制攻撃】を行ったものとしては扱わないため、敵の反応は【死ぬまで戦う】へ変更しない。"
if s.count(old) != 1:
    raise SystemExit(f"Event61 neutral combat anchor count must be 1, got {s.count(old)}")
s = s.replace(old, new, 1)
scenario.write_text(s, encoding="utf-8")

audit = Path("docs/SCENARIO_V1_01_RESOURCE_BALANCE_AUDIT.md")
a = audit.read_text(encoding="utf-8")
heading = "## 49. Black Sun 出目61【中立】後の戦闘開始と先攻 — 採用済み"
section = """

## 49. Black Sun 出目61【中立】後の戦闘開始と先攻 — 採用済み

ユーザー承認により、出目61【交差点の支配者】で反応【中立】を確認した後、プレイヤー側から戦闘を開始する場合の処理を明確化する。

- 【中立】確認後に戦闘を開始する場合、敵の反応を【敵対的】として扱う。
- 戦闘開始時の行動順は分隊側を先攻とする。
- この先攻は行動順だけを変更するシナリオ固有指定であり、Core v1.01の遭遇時選択【先制攻撃】を後から選び直したものとしては扱わない。
- したがって、この処理だけを理由として敵の反応を【死ぬまで戦う】へ変更しない。
- 出目61は高脅威目標であるため、【敵対的】になってもCore v1.01の敵戦闘集団用の自動撤退条件は適用しない。

これにより、反応確認後の任意交戦とCore v1.01の遭遇時選択【先制攻撃】を区別し、【反応】と【行動順】を独立して処理する既存方針と整合させる。
"""
if heading not in a:
    a = a.rstrip() + section + "\n"
audit.write_text(a, encoding="utf-8")
