from pathlib import Path

scenario = Path("scenarios/missions/d66_lvl10-16_mission_01_blacksun.md")
s = scenario.read_text(encoding="utf-8")
old = """- 民兵 1 + 1d3 名[地上]\n- レベル：5\n- 戦利品：戦利品表を振る。\n"""
new = """- 民兵 1 + 1d3 名[地上]\n- レベル：5\n- 反応：死ぬまで戦う\n- 戦利品：戦利品表を振る。\n"""
if s.count(old) != 1:
    raise SystemExit(f"final3 reaction block count must be 1, got {s.count(old)}")
scenario.write_text(s.replace(old, new, 1), encoding="utf-8")

audit = Path("docs/SCENARIO_V1_01_RESOURCE_BALANCE_AUDIT.md")
a = audit.read_text(encoding="utf-8")
heading = "## 36. Black Sun 3周目最終戦の反応 — 採用済み"
section = """

## 36. Black Sun 3周目最終戦の反応 — 採用済み

ユーザー承認により、3周目最終戦の反応を【死ぬまで戦う】に固定する。

- 対戦車砲装甲車両と同行する民兵を含む、この最終戦全体の反応を【死ぬまで戦う】として扱う。
- 民兵はCore v1.01の半数以下による自動撤退を行わない。
- 装甲車両の生命点を0にした場合は、既存のシナリオ固有処理を優先し、車両が炎上して民兵が潰走し、その時点で戦闘終了とする。
- 民兵を全滅させても装甲車両が残っている限り、装甲車両との戦闘は継続する。
- 既存の攻撃対象決定、DMR、【精密射撃】、対戦車砲の着弾対象ロール等は変更しない。

これにより、この最終戦では民兵の通常撤退ではなく、装甲車両の撃破が戦闘を一気に終わらせる主要な突破条件となる。
"""
if heading not in a:
    audit.write_text(a.rstrip() + section + "\n", encoding="utf-8")
