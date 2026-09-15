from pathlib import Path

scenario = Path("scenarios/missions/d66_lvl10-16_mission_01_blacksun.md")
s = scenario.read_text(encoding="utf-8")
old = """- 挟撃効果：
  地上と側面の民兵がともに1名以上生存している間、分隊の防御ロールに -1 の修正を与える。
"""
new = """- 挟撃効果：
  地上と側面の民兵がともに1名以上生存している間、分隊の防御ロールに -1 の修正を与える。
- 撤退判定：
  地上の民兵と側面の民兵は、配置のみが異なる1つの【敵戦闘集団】として扱う。初期人数は「地上2名＋戦闘開始時に決定した側面民兵数」の合計とする。反応が【敵対的】の場合、地上・側面を合計した現在人数が初期合計人数の半分以下になった時点で、生存している民兵はまとめて撤退する。反応が【死ぬまで戦う】の場合は撤退しない。
"""
if s.count(old) != 1:
    raise SystemExit(f"event53 marker count must be 1, got {s.count(old)}")
scenario.write_text(s.replace(old, new, 1), encoding="utf-8")

audit = Path("docs/SCENARIO_V1_01_RESOURCE_BALANCE_AUDIT.md")
a = audit.read_text(encoding="utf-8")
heading = "## 22. Black Sun 出目53の撤退判定 — 採用済み"
section = """

## 22. Black Sun 出目53の撤退判定 — 採用済み

ユーザー承認により、出目53【挟撃】では地上民兵と側面民兵を、撤退判定上は配置のみが異なる1つの【敵戦闘集団】として扱う。

- 初期人数は「地上2名＋戦闘開始時に決定した側面民兵 `1d3` 名」の合計。
- 攻撃対象の指定、側面への攻撃ロール -1、両方向が残っている間の防御ロール -1 は変更しない。
- 反応が【敵対的】の場合、地上・側面を合計した現在人数が初期合計人数の半分以下になった時点で、生存民兵はまとめて撤退する。
- 反応が【死ぬまで戦う】の場合、半数以下でも撤退しない。

これにより、一方の配置だけが半数以下になったことで他方の民兵まで即座に戦闘終了となる不自然な解釈を避け、Core v1.01の撤退基準を維持する。
"""
if heading not in a:
    audit.write_text(a.rstrip() + section + "\n", encoding="utf-8")
