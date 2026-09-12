from pathlib import Path

scenario = Path("scenarios/missions/d66_lvl10-16_mission_01_blacksun.md")
text = scenario.read_text(encoding="utf-8")
old = "- 攻撃ロールの達成値が奇数の場合は走行車両、偶数の場合は民兵に命中する。対象が倒された後は自動的にもう片方の敵へ命中する。"
new = "- 攻撃対象：通常の攻撃では、【攻撃ロール】の達成値が奇数の場合は装甲車両、偶数の場合は民兵に命中する。いずれかの対象が倒された後は、自動的に残った対象へ命中する。【精密射撃】を使用した分隊長、または常時【精密射撃】が発動しているマークスマンは、この奇数／偶数による命中先決定を無視し、攻撃ロール前に装甲車両または民兵のどちらを攻撃するか選択できる。"
if text.count(old) != 1:
    raise SystemExit(f"target count must be 1, got {text.count(old)}")
scenario.write_text(text.replace(old, new, 1), encoding="utf-8")

audit = Path("docs/SCENARIO_V1_01_RESOURCE_BALANCE_AUDIT.md")
a = audit.read_text(encoding="utf-8")
section = """

## 13. Black Sun 3周目最終戦の精密射撃 — 採用済み

ユーザー承認により、3周目最終戦の装甲車両／民兵の命中先決定では、通常攻撃は達成値の奇数／偶数で対象を決めますが、【精密射撃】はこの制限を無視します。

- 通常攻撃：達成値が奇数なら装甲車両、偶数なら民兵に命中する。
- 片方の対象が倒された後は、以後の命中先は残った対象へ自動的に切り替わる。
- 【精密射撃】を使用した分隊長は、攻撃ロール前に装甲車両／民兵のどちらを攻撃するか選べる。
- 常時【精密射撃】を持つマークスマンも同様に対象を選べる。

これにより、混戦による不確実性を残しながら、【精密射撃】の戦術的価値を維持します。
"""
heading = "## 13. Black Sun 3周目最終戦の精密射撃 — 採用済み"
if heading not in a:
    audit.write_text(a.rstrip() + section + "\n", encoding="utf-8")
