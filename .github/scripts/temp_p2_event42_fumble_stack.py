from pathlib import Path

scenario = Path("scenarios/missions/d66_lvl10-16_mission_01_blacksun.md")
s = scenario.read_text(encoding="utf-8")
old = """- 成功：転倒するが爆発は免れる。何も起こらない。
- 失敗：小爆発が起きる。対象が分隊員の場合、その隊員は次の戦闘の最初のラウンドにおいて攻撃ロールを行うことができない。対象が分隊長の場合、分隊長は次の戦闘の第1ラウンドに攻撃ロールを行うことができない。
- 失敗(ファンブル)：爆発が直撃する。対象は1ダメージを受ける。
"""
new = """- 成功：転倒するが爆発は免れる。何も起こらない。
- 失敗：小爆発が起きる。対象が分隊員の場合、その隊員は次の戦闘の最初のラウンドにおいて攻撃ロールを行うことができない。対象が分隊長の場合、分隊長は次の戦闘の第1ラウンドに攻撃ロールを行うことができない。
- 失敗(ファンブル)：上記の通常失敗の効果を適用したうえで、爆発が直撃し、対象は追加で1ダメージを受ける。
"""
if s.count(old) != 1:
    raise SystemExit(f"event42 outcome block count must be 1, got {s.count(old)}")
scenario.write_text(s.replace(old, new, 1), encoding="utf-8")

audit = Path("docs/SCENARIO_V1_01_RESOURCE_BALANCE_AUDIT.md")
a = audit.read_text(encoding="utf-8")
heading = "## 35. Black Sun 出目42のファンブル効果 — 採用済み"
section = """

## 35. Black Sun 出目42のファンブル効果 — 採用済み

ユーザー判断により、出目42【トリップワイヤー】の防御ロールがファンブルだった場合は、通常失敗効果とファンブル追加効果を重複適用する。

- 通常失敗では、対象者は次の戦闘の第1ラウンドに【攻撃ロール】を行えない。
- ファンブルでもこの通常失敗効果を適用する。
- そのうえでファンブル追加効果として、対象者は1ダメージを受ける。
- 対象が分隊員でも、Core v1.01の共通フォールバックにより分隊長になった場合でも同様に処理する。

これにより、出目44【崩落危険区域】と同様に、ファンブルを「通常失敗より重い追加結果」として一貫して扱う。
"""
if heading not in a:
    audit.write_text(a.rstrip() + section + "\n", encoding="utf-8")
