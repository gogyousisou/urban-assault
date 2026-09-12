from pathlib import Path

scenario = Path("scenarios/missions/d66_lvl10-16_mission_01_blacksun.md")
text = scenario.read_text(encoding="utf-8")
old = "- 2ラウンド開始時に1d3体の民兵が追加。"
new = "- 増援：第1ラウンド終了時点で民兵が1名以上生存している場合のみ、第2ラウンド開始時に民兵1d3名を追加する。第1ラウンド中に初期民兵を全滅させた場合、その時点で戦闘は終了し、増援は出現しない。"
if text.count(old) != 1:
    raise SystemExit(f"target count must be 1, got {text.count(old)}")
scenario.write_text(text.replace(old, new, 1), encoding="utf-8")

audit = Path("docs/SCENARIO_V1_01_RESOURCE_BALANCE_AUDIT.md")
a = audit.read_text(encoding="utf-8")
section = """

## 12. Black Sun 1周目最終イベントの増援 — 採用済み

ユーザー承認により、1周目最終イベントは固定の波状防衛戦にはせず、初期民兵を第1ラウンド中に全滅させた場合は迅速な制圧成功として扱います。

- 第1ラウンド終了時点で民兵が1名以上生存している場合のみ、第2ラウンド開始時に民兵 `1d3` 名を追加する。
- 第1ラウンド中に初期民兵を全滅させた場合、その時点で戦闘終了とし、増援は出現しない。
- クリティカル連鎖、数的優位、航空支援等による高火力が成功した場合、その成果を早期制圧として認める。

これにより、1周目は「素早く制圧できれば増援を阻止できる戦闘」、2周目は「敵を一時的に0名にしても3ラウンド継続する波状防衛戦」と役割を分けます。
"""
heading = "## 12. Black Sun 1周目最終イベントの増援 — 採用済み"
if heading not in a:
    audit.write_text(a.rstrip() + section + "\n", encoding="utf-8")
