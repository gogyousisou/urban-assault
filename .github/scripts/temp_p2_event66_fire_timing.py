from pathlib import Path

scenario = Path("scenarios/missions/d66_lvl10-16_mission_01_blacksun.md")
s = scenario.read_text(encoding="utf-8")
old = """- 追い込み火力：
  残り生命点が2以下になった場合、攻撃回数は2になる。
"""
new = """- 追い込み火力：
  敵側が行動を開始する時点の残り生命点を参照する。残り生命点が2以下なら、その敵側行動での攻撃回数は2になる。残り生命点が3以上なら攻撃回数は1のままとする。分隊側が先攻し、その敵側行動より前に生命点を2以下へ減らした場合は、同じラウンドから攻撃回数2を適用する。敵側がすでにそのラウンドの行動を終えた後で生命点が2以下になった場合は、次に敵側が行動する時から適用する。
"""
if s.count(old) != 1:
    raise SystemExit(f"Event66 anchor count={s.count(old)}")
s = s.replace(old, new, 1)
scenario.write_text(s, encoding="utf-8")

audit = Path("docs/SCENARIO_V1_01_RESOURCE_BALANCE_AUDIT.md")
a = audit.read_text(encoding="utf-8")
heading = "## 61. Black Sun 出目66【追い込み火力】の判定時点 — 整合明確化済み"
section = """

## 61. Black Sun 出目66【追い込み火力】の判定時点 — 整合明確化済み

出目66【即席装甲ガン・トラック】の「残り生命点が2以下になった場合、攻撃回数は2になる」は、生命点が閾値を跨いだラウンドでいつ増加するかが未記載だったため、既存効果の発動時点を明確化する。

- 敵側が行動を開始する時点の残り生命点で、その敵側行動の攻撃回数を確定する。
- 残り生命点3以上なら攻撃回数1、2以下なら攻撃回数2とする。
- 分隊側が先攻し、敵側行動の前に生命点を2以下へ減らした場合は、その同じラウンドの敵側行動から攻撃回数2になる。
- 敵側が先に行動を終え、その後に生命点が2以下へ減少した場合は、次回の敵側行動から攻撃回数2になる。
- 生命点1で【ネゴシエーション】に成功して車両が戦闘から除外された場合は、当然ながら以後の攻撃は発生しない。

これは「残り生命点が2以下になった場合」という既存条件を、敵の攻撃回数を実際に確定する時点へ接続する明確化であり、新しい追加攻撃やラウンド外攻撃を発生させるものではない。
"""
if heading not in a:
    a = a.rstrip() + section + "\n"
audit.write_text(a, encoding="utf-8")
