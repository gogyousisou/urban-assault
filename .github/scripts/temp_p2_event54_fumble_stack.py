from pathlib import Path

scenario = Path("scenarios/missions/d66_lvl10-16_mission_01_blacksun.md")
s = scenario.read_text(encoding="utf-8")
old = """- 即席爆弾：  \n  第0ラウンドに1d6を振る。  \n  出目1の場合、IEDが爆発する。  \n  分隊長は即座に防御ロールを行う。  \n  防御に失敗した場合、通常のダメージに加えて【負傷+1】を受ける。\n"""
new = """- 即席爆弾：  \n  第0ラウンドに1d6を振る。  \n  出目1の場合、IEDが爆発する。  \n  分隊長は即座に防御ロールを行う。  \n  防御に失敗した場合、通常のダメージに加えて【負傷+1】を受ける。防御ロールがファンブル（出目1）だった場合は、Core v1.01のファンブルによる【負傷+1】も重複するため、合計【負傷+2】を受ける。\n"""
if s.count(old) != 1:
    raise SystemExit(f"event54 target count must be 1, got {s.count(old)}")
scenario.write_text(s.replace(old, new, 1), encoding="utf-8")

audit = Path("docs/SCENARIO_V1_01_RESOURCE_BALANCE_AUDIT.md")
a = audit.read_text(encoding="utf-8")
heading = "## 23. Black Sun 出目54のIEDファンブル負傷 — 採用済み"
section = """

## 23. Black Sun 出目54のIEDファンブル負傷 — 採用済み

ユーザー承認により、出目54【民衆の悪意】の即席爆弾に対する防御ロールでは、シナリオ固有の負傷とCore v1.01のファンブル負傷を重複適用する。

- IEDが作動した場合、分隊長は通常どおり防御ロールを行う。
- 通常の防御失敗では、通常ダメージに加えて【負傷+1】。
- 防御ロールがファンブル（出目1）だった場合は、シナリオ固有の【負傷+1】にCore v1.01のファンブル【負傷+1】を加え、合計【負傷+2】。
- Core側のファンブル処理をこのイベントだけ例外化しない。

これにより、IED直撃のファンブルは低確率だが重大な結果となり、シナリオ固有効果とCoreの基本処理を同時に維持する。
"""
if heading not in a:
    audit.write_text(a.rstrip() + section + "\n", encoding="utf-8")
