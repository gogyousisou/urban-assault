from pathlib import Path

scenario = Path("scenarios/missions/d66_lvl10-16_mission_01_blacksun.md")
s = scenario.read_text(encoding="utf-8")
marker = "分隊員にコンバットエンジニアがいる場合は器用ロールに+2の修正を与える。"
if s.count(marker) != 1:
    raise SystemExit(f"event41 +2 marker count must be 1, got {s.count(marker)}")

audit = Path("docs/SCENARIO_V1_01_RESOURCE_BALANCE_AUDIT.md")
a = audit.read_text(encoding="utf-8")
heading = "## 38. Black Sun 出目41のコンバットエンジニア補正 — 現行+2維持"
section = """

## 38. Black Sun 出目41のコンバットエンジニア補正 — 現行+2維持

ユーザー判断により、出目41【薄暗い部屋】のIED解除時にコンバットエンジニアがいる場合の補正は、Core v1.01の一般的な【トラップ解除判定+1】ではなく、シナリオ固有の【器用ロール+2】を維持する。

- 出目41の解除判定は【器用ロール】目標値4のまま変更しない。
- コンバットエンジニアがいる場合は、現行どおりこの器用ロールに+2する。
- Core v1.01の一般能力【トラップ解除判定+1】とは重複させず、シナリオ固有の+2が置き換えるものとして扱う。
- シナリオ優先原則に基づく意図的な例外として記録する。

これにより、出目41では工兵がIED解除に特に有利なシナリオ固有設計を維持する。
"""
if heading not in a:
    audit.write_text(a.rstrip() + section + "\n", encoding="utf-8")
