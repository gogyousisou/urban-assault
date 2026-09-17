from pathlib import Path

scenario = Path("scenarios/missions/d66_lvl10-16_mission_01_blacksun.md")
s = scenario.read_text(encoding="utf-8")

old43 = "分隊長並びに分隊員全員が防御ロール（目標値：3）を行う。"
new43 = "分隊長と、その場に同行している生存戦闘員が防御ロール（目標値：3）を行う。非戦闘員、および分隊に同行せず狙撃ポイントで待機しているスナイパー／スポッターは対象外とする。"
if s.count(old43) != 1:
    raise SystemExit(f"event43 participant marker count must be 1, got {s.count(old43)}")
s = s.replace(old43, new43, 1)

old44 = "  全員が防御ロール（目標値：3）を行う。"
new44 = "  分隊長と、その場に同行している生存戦闘員が防御ロール（目標値：3）を行う。非戦闘員、および分隊に同行せず狙撃ポイントで待機しているスナイパー／スポッターは対象外とする。"
if s.count(old44) != 1:
    raise SystemExit(f"event44 participant marker count must be 1, got {s.count(old44)}")
s = s.replace(old44, new44, 1)

scenario.write_text(s, encoding="utf-8")

audit = Path("docs/SCENARIO_V1_01_RESOURCE_BALANCE_AUDIT.md")
a = audit.read_text(encoding="utf-8")
heading = "## 37. Black Sun 出目43・44の防御ロール対象 — 採用済み"
section = """

## 37. Black Sun 出目43・44の防御ロール対象 — 採用済み

ユーザー承認により、出目43【遠隔起爆】と出目44【崩落危険区域】で防御ロールを行う「全員」の範囲を明確化する。

- 防御ロールを行うのは、分隊長と、その場に同行している生存戦闘員のみとする。
- K9や現地協力者等の非戦闘員は対象外とする。
- Core v1.01で「分隊には同行せず、狙撃ポイントで待機」と定義されているスナイパーおよびスポッターも対象外とする。
- 出目43の通常失敗時／ファンブル時に行う【被弾ロール】の処理は変更しない。
- 出目44の通常失敗効果、ファンブル時の追加【被弾ロール】、対象0名時の分隊長フォールバックは変更しない。

これにより、現場に存在しない隊員や通常戦闘に参加しない非戦闘員が、トラップの一斉防御判定だけ対象になる解釈を排除する。非戦闘員へ直接被害を与えるイベントを設計する場合は、シナリオ側で個別に明記する。
"""
if heading not in a:
    audit.write_text(a.rstrip() + section + "\n", encoding="utf-8")
