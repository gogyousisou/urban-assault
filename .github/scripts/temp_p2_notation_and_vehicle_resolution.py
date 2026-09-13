from pathlib import Path

core = Path("core/core-rule-full.md")
c = core.read_text(encoding="utf-8")
old = """`1d3` を求める場合は 1d6 を振り、1～2 を 1、3～4 を 2、5～6 を 3 として扱います。\n\n`d66` は 1d6 を 2 回振り、最初の出目を十の位、次の出目を一の位として 11～66 の結果を作る方法です。\n"""
new = """`1d2` を求める場合は 1d6 を振り、1～3 を 1、4～6 を 2 として扱います。\n\n`1d3` を求める場合は 1d6 を振り、1～2 を 1、3～4 を 2、5～6 を 3 として扱います。\n\n`d66` は 1d6 を 2 回振り、最初の出目を十の位、次の出目を一の位として 11～66 の結果を作る方法です。\n"""
if c.count(old) != 1:
    raise SystemExit(f"core dice target count must be 1, got {c.count(old)}")
core.write_text(c.replace(old,new,1), encoding="utf-8")

scenario = Path("scenarios/missions/d66_lvl10-16_mission_01_blacksun.md")
s = scenario.read_text(encoding="utf-8")
old2 = """    - 対戦車砲が攻撃するたび、防御ロールの前に【着弾対象ロール】として1d6を振る。奇数なら分隊長、偶数なら分隊員側を攻撃対象とする。\n"""
new2 = """    - 対戦車砲の攻撃は民兵の攻撃回数とは合算せず、独立して処理する。対戦車砲が攻撃するたび、防御ロールの前に【着弾対象ロール】として1d6を振る。奇数なら分隊長、偶数なら分隊員側を攻撃対象とする。民兵側の攻撃はCore v1.01の通常の【敵戦闘集団】として処理する。\n"""
if s.count(old2) != 1:
    raise SystemExit(f"vehicle target count must be 1, got {s.count(old2)}")
scenario.write_text(s.replace(old2,new2,1), encoding="utf-8")

audit = Path("docs/SCENARIO_V1_01_RESOURCE_BALANCE_AUDIT.md")
a = audit.read_text(encoding="utf-8")
section = """

## 17. 1d2表記と3周目最終戦の敵攻撃分離 — 明確化済み

追加監査で、Black Sun の出目22・24などに `1d2` が使われている一方、Core v1.01 のサイコロ表記には `1d2` の換算方法が未記載であることを確認しました。既存の出目幅を変更せずプレイ可能にするため、Core 06章に「1d6の1～3を1、4～6を2」とする `1d2` の換算方法を追加しました。

また、3周目最終戦では対戦車砲の【着弾対象ロール】をCoreの通常攻撃配分と混同しないよう、次を明確化しました。

- 対戦車砲の1回の攻撃は、民兵の攻撃回数とは合算せず独立処理する。
- 対戦車砲は承認済みの【着弾対象ロール】で対象を決める。
- 民兵側の攻撃はCore v1.01の通常の【敵戦闘集団】として処理する。

いずれも既存の敵数・ダメージ量・出現確率は変更していません。
"""
heading = "## 17. 1d2表記と3周目最終戦の敵攻撃分離 — 明確化済み"
if heading not in a:
    audit.write_text(a.rstrip() + section + "\n", encoding="utf-8")
