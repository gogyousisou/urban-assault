from pathlib import Path

scenario = Path("scenarios/missions/d66_lvl10-16_mission_01_blacksun.md")
text = scenario.read_text(encoding="utf-8")
old = """- 2ラウンド目以降、ラウンド開始時に民兵 2 + 1d3 名[地上]が追加される。\n- 3ラウンド終了後、救出部隊が到着し周辺を制圧する為戦闘が終了する。\n- 組織的防衛：分隊員の生存数により、防御ロールに次の修正を与える。 【1-2名：+0】【3-5名：+1】【6以上：+2】\n"""
new = """- 2ラウンド目以降、ラウンド開始時に民兵 2 + 1d3 名[地上]が追加される。\n- 波状防衛：このイベントでは、ラウンド途中で民兵が一時的に0名になっても戦闘は終了しない。敵が0名の間は敵からの攻撃は発生しないが、次のラウンド開始時には予定どおり増援を追加する。3ラウンド終了時まで戦闘を継続する。\n- 3ラウンド終了後、救出部隊が到着し周辺を制圧する為戦闘が終了する。\n- 組織的防衛：分隊員の生存数により、防御ロールに次の修正を与える。 【1-2名：+0】【3-5名：+1】【6以上：+2】\n"""
if old not in text:
    raise SystemExit("target scenario block not found")
scenario.write_text(text.replace(old, new, 1), encoding="utf-8")

audit = Path("docs/SCENARIO_V1_01_RESOURCE_BALANCE_AUDIT.md")
a = audit.read_text(encoding="utf-8")
section = """

## 11. Black Sun 2周目最終イベントの波状防衛 — 採用済み

ユーザー承認により、2周目最終イベントは3ラウンド固定の波状防衛戦として扱います。

- ラウンド途中で民兵が一時的に0名になっても、その時点では戦闘終了としない。
- 敵が0名の間は敵からの攻撃は発生しない。
- 2ラウンド目および3ラウンド目の開始時には、予定どおり民兵 `2 + 1d3` 名の増援を追加する。
- 3ラウンド終了後、救出部隊到着により戦闘終了とする。

これにより、クリティカル連鎖や航空支援で一時的に敵を全滅させた場合でも、成果は「早期終了」ではなく次の増援波への安全余裕として扱います。
"""
if "## 11. Black Sun 2周目最終イベントの波状防衛 — 採用済み" not in a:
    audit.write_text(a.rstrip() + section + "\n", encoding="utf-8")
