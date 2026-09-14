from pathlib import Path

scenario = Path("scenarios/missions/d66_lvl10-16_mission_01_blacksun.md")
s = scenario.read_text(encoding="utf-8")
old = """- B：突破する  
  全員が防御ロール（目標値：3）を行う。
  - 失敗者が出た場合：次の戦闘の第1ラウンド、分隊の攻撃ロールに -1 の修正を与える。
  - ファンブルが出た場合：被弾ロールを1回行う。
"""
new = """- B：突破する  
  全員が防御ロール（目標値：3）を行う。
  - 失敗者が出た場合：次の戦闘の第1ラウンド、分隊の攻撃ロールに -1 の修正を与える。
  - ファンブルが1回以上出た場合：上記の効果に加えて【被弾ロール】を1回行い、対象となった分隊員は1ダメージを受ける。ファンブルが複数回出ても【被弾ロール】は1回のみ行う。攻撃対象となれる分隊員が1名もいない場合は、分隊長が1ダメージを受ける。
"""
if s.count(old) != 1:
    raise SystemExit(f"event44 target count must be 1, got {s.count(old)}")
scenario.write_text(s.replace(old, new, 1), encoding="utf-8")

audit = Path("docs/SCENARIO_V1_01_RESOURCE_BALANCE_AUDIT.md")
a = audit.read_text(encoding="utf-8")
heading = "## 20. Black Sun 出目44のファンブル処理 — 採用済み"
section = """

## 20. Black Sun 出目44のファンブル処理 — 採用済み

ユーザー承認により、出目44【崩落危険区域】で突破を選び、防御ロールにファンブルが出た場合のダメージ処理を明確化する。

- 防御ロールの失敗者が1名以上出た場合、既存どおり次の戦闘の第1ラウンドに分隊の攻撃ロール -1。
- ファンブルが1回以上出た場合は、上記に加えて【被弾ロール】を1回行う。
- 対象となった分隊員は1ダメージを受ける。
- ファンブルが複数回出ても【被弾ロール】は1回のみ。
- 攻撃対象となれる分隊員が1名もいない場合は、分隊長が1ダメージを受ける。

これにより、通常失敗は次戦闘への一時的不利、ファンブルはさらに実ダメージを伴う段階的な危険として処理する。
"""
if heading not in a:
    audit.write_text(a.rstrip() + section + "\n", encoding="utf-8")
