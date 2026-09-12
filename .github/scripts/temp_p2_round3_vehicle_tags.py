from pathlib import Path

scenario = Path("scenarios/missions/d66_lvl10-16_mission_01_blacksun.md")
text = scenario.read_text(encoding="utf-8")
old = """- 対戦車砲装甲車両\n  - レベル：5\n  - 生命点：4\n  - 攻撃回数：1(奇数ラウンドのみ)\n"""
new = """- 対戦車砲装甲車両<高脅威目標>\n  - 属性：車両・装甲\n  - レベル：5\n  - 生命点：4\n  - 攻撃回数：1(奇数ラウンドのみ)\n"""
if text.count(old) != 1:
    raise SystemExit(f"target count must be 1, got {text.count(old)}")
scenario.write_text(text.replace(old, new, 1), encoding="utf-8")

audit = Path("docs/SCENARIO_V1_01_RESOURCE_BALANCE_AUDIT.md")
a = audit.read_text(encoding="utf-8")
section = """

## 14. Black Sun 3周目最終戦の装甲車両分類 — 採用済み

ユーザー承認により、3周目最終戦の対戦車砲装甲車両を明示的に【高脅威目標】として扱い、属性に「車両・装甲」を付与します。

- 対戦車砲装甲車両は高脅威目標。
- 属性は「車両・装甲」。
- レベル5、生命点4、攻撃回数1（奇数ラウンドのみ）は変更しない。
- コンバットエンジニアIED、AT4、AMRなど、車両・装甲を参照する効果の対象になる。

これは既存能力値の強化・弱体化ではなく、コアルール上の対象分類を明確にするための修正です。
"""
heading = "## 14. Black Sun 3周目最終戦の装甲車両分類 — 採用済み"
if heading not in a:
    audit.write_text(a.rstrip() + section + "\n", encoding="utf-8")
