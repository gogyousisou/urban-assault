from pathlib import Path

scenario = Path("scenarios/missions/d66_lvl10-16_mission_01_blacksun.md")
s = scenario.read_text(encoding="utf-8")
old = """### 3周目

_車列の陰に隠れながら広場を駆け抜けたレンジャー部隊。_"""
start = s.index(old)
end = s.index("## 14. 最終イベント", start)
block = s[start:end]
if block.count("- 戦利品：\n") != 1:
    raise SystemExit(f"third-loop blank loot count must be 1, got {block.count('- 戦利品：\\n')}")
block = block.replace("- 戦利品：\n", "- 戦利品：なし\n", 1)
s = s[:start] + block + s[end:]
scenario.write_text(s, encoding="utf-8")

audit = Path("docs/SCENARIO_V1_01_RESOURCE_BALANCE_AUDIT.md")
a = audit.read_text(encoding="utf-8")
heading = "## 18. Black Sun 3周目中間イベントの戦利品 — 採用済み"
section = """

## 18. Black Sun 3周目中間イベントの戦利品 — 採用済み

ユーザー判断により、3周目中間イベントの民兵戦は「戦利品：なし」とします。

- 撤収中に車列から取り残され、そのまま走り続ける場面であるため、戦闘後の物資回収は行わない。
- 民兵 `6 + 1d3` 名、レベル5、反応【敵対的】の戦闘条件は変更しない。
- 直後の3周目最終イベントに向けた追加補給は発生しない。

以後の資源収支テストでは、この中間イベントからの弾倉・軍票等の回収を0として扱います。
"""
if heading not in a:
    audit.write_text(a.rstrip() + section + "\n", encoding="utf-8")
