from pathlib import Path

scenario = Path("scenarios/missions/d66_lvl10-16_mission_01_blacksun.md")
s = scenario.read_text(encoding="utf-8")
old = "- 組織的防衛：分隊員の生存数により、防御ロールに次の修正を与える。 【1-2名：+0】【3-5名：+1】【6以上：+2】"
new = "- 組織的防衛：各ラウンド開始時、そのラウンドに戦闘参加可能な生存戦闘員数により、防御ロールに次の修正を与える。分隊長および非戦闘員は人数に含めない。また、出目46【車両IED】等の効果によりそのラウンドだけ戦闘に参加できない戦闘員も、そのラウンドの人数には含めない。 【1-2名：+0】【3-5名：+1】【6以上：+2】"
if s.count(old) != 1:
    raise SystemExit(f"organized defense marker count must be 1, got {s.count(old)}")
scenario.write_text(s.replace(old, new, 1), encoding="utf-8")

audit = Path("docs/SCENARIO_V1_01_RESOURCE_BALANCE_AUDIT.md")
a = audit.read_text(encoding="utf-8")
heading = "## 34. Black Sun 2周目最終戦の組織的防衛人数 — 採用済み"
section = """

## 34. Black Sun 2周目最終戦の組織的防衛人数 — 採用済み

ユーザー承認により、2周目最終戦【組織的防衛】の人数判定を「分隊員の生存数」から、「そのラウンドに戦闘参加可能な生存戦闘員数」へ明確化する。

- 分隊長は人数に含めない。
- 非戦闘員はCore v1.01どおり戦闘不参加のため人数に含めない。
- 生存していても、そのラウンドに戦闘参加できない戦闘員は人数に含めない。
- 出目46【車両IED】等で第1ラウンドのみ参加不可になっている戦闘員は、第1ラウンドの人数から除外し、第2ラウンド以降に通常復帰した場合は再び数える。
- 防御ロール修正値は既存どおり【1-2名：+0】【3-5名：+1】【6以上：+2】とし、数値自体は変更しない。

これにより、K9や現地協力者などの非戦闘員を編成しただけで【組織的防衛】の補正が上昇する解釈を排除し、実際にそのラウンドの防御戦闘へ参加できる戦闘員数を反映する。
"""
if heading not in a:
    audit.write_text(a.rstrip() + section + "\n", encoding="utf-8")
