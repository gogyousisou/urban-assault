from pathlib import Path

scenario = Path("scenarios/missions/d66_lvl10-16_mission_01_blacksun.md")
s = scenario.read_text(encoding="utf-8")
old = "- 攻撃対象：通常の攻撃では、【攻撃ロール】の達成値が奇数の場合は装甲車両、偶数の場合は民兵に命中する。いずれかの対象が倒された後は、自動的に残った対象へ命中する。【精密射撃】を使用した分隊長、または常時【精密射撃】が発動しているマークスマンは、この奇数／偶数による命中先決定を無視し、攻撃ロール前に装甲車両または民兵のどちらを攻撃するか選択できる。"
new = "- 攻撃対象：通常の攻撃では、【攻撃ロール】の達成値が奇数の場合は装甲車両、偶数の場合は民兵に命中する。いずれかの対象が倒された後は、自動的に残った対象へ命中する。DMRを使用した攻撃はCore v1.01の固有効果を適用し、達成値が奇数の場合は装甲車両または民兵のどちらにダメージを与えるか選択できる。達成値が偶数の場合は通常どおり民兵に命中する。【精密射撃】を使用した分隊長、または常時【精密射撃】が発動しているマークスマンは、この奇数／偶数による命中先決定を無視し、攻撃ロール前に装甲車両または民兵のどちらを攻撃するか選択できる。"
if s.count(old) != 1:
    raise SystemExit(f"targeting marker count must be 1, got {s.count(old)}")
scenario.write_text(s.replace(old, new, 1), encoding="utf-8")

audit = Path("docs/SCENARIO_V1_01_RESOURCE_BALANCE_AUDIT.md")
a = audit.read_text(encoding="utf-8")
heading = "## 26. Black Sun 3周目最終戦のDMR対象選択 — 採用済み"
section = """

## 26. Black Sun 3周目最終戦のDMR対象選択 — 採用済み

ユーザー承認により、3周目最終戦でもCore v1.01のDMR固有効果を有効とする。

- 通常攻撃は従来どおり、達成値が奇数なら装甲車両、偶数なら民兵に命中する。
- DMRを使用した攻撃で達成値が奇数の場合、Core v1.01の固有効果により装甲車両または民兵のどちらにダメージを与えるか選択できる。
- DMRの達成値が偶数の場合はシナリオ通常処理に従い、民兵に命中する。
- 【精密射撃】を使用した分隊長、または常時【精密射撃】が発動するマークスマンは、従来どおり攻撃ロール前に対象を選択できる。
- したがって、DMRは「奇数達成値の場合のみ攻撃後に対象選択」、【精密射撃】は「出目に関係なく攻撃前に対象選択」として役割差を維持する。

これにより、DMRの混成目標に対する限定的な精密性を、この最終戦だけ失わせずに処理する。
"""
if heading not in a:
    audit.write_text(a.rstrip() + section + "\n", encoding="utf-8")
