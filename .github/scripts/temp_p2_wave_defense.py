from pathlib import Path

scenario = Path("scenarios/missions/d66_lvl10-16_mission_01_blacksun.md")
text = scenario.read_text(encoding="utf-8")
old = """- 2ラウンド目以降、ラウンド開始時に民兵 2 + 1d3 名[地上]が追加される。\n- 3ラウンド終了後、救出部隊が到着し周辺を制圧する為戦闘が終了する。\n- 組織的防衛：分隊員の生存数により、防御ロールに次の修正を与える。 【1-2名：+0】【3-5名：+1】【6以上：+2】\n"""
new = """- 2ラウンド目以降、ラウンド開始時に民兵 2 + 1d3 名[地上]が追加される。\n- 波状防衛：このイベントでは、ラウンド途中で民兵が一時的に0名になっても戦闘は終了しない。敵が0名の間は敵からの攻撃は発生しないが、次のラウンド開始時には予定どおり増援を追加する。3ラウンド終了時まで戦闘を継続する。\n- 3ラウンド終了後、救出部隊が到着し周辺を制圧する為戦闘が終了する。\n- 組織的防衛：分隊員の生存数により、防御ロールに次の修正を与える。 【1-2名：+0】【3-5名：+1】【6以上：+2】\n"""
if old not in text:
    raise SystemExit("target scenario block not found")
scenario.write_text(text.replace(old, new, 1), encoding="utf-8")

audit = Path("docs/SCENARIO_V1_01_RESOURCE_BALANCE_AUDIT.md")
a = audit.read_text(encoding="utf-8")n