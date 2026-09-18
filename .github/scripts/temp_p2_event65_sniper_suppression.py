from pathlib import Path

scenario = Path("scenarios/missions/d66_lvl10-16_mission_01_blacksun.md")
s = scenario.read_text(encoding="utf-8")
old = """- 機銃制圧：
  激しい掃射により反撃がままならない。1ラウンドに攻撃ロールを行えるのは分隊長を含め最大3名までとする。
"""
new = """- 機銃制圧：
  激しい掃射により反撃がままならない。1ラウンドに攻撃ロールを行えるのは分隊長を含め最大3名までとする。狙撃ポイントで待機しているスナイパーはこの3名の上限に含めず、屋外戦闘の参加条件を満たしている限り別枠で通常どおり攻撃できる。
"""
if s.count(old) != 1:
    raise SystemExit(f"Event65 anchor count={s.count(old)}")
s = s.replace(old, new, 1)
scenario.write_text(s, encoding="utf-8")

audit = Path("docs/SCENARIO_V1_01_RESOURCE_BALANCE_AUDIT.md")
a = audit.read_text(encoding="utf-8")
heading = "## 59. Black Sun 出目65【機銃制圧】とスナイパー — 採用済み"
section = """

## 59. Black Sun 出目65【機銃制圧】とスナイパー — 採用済み

ユーザー承認により、出目65【つぎはぎだらけの武装トラック】の【機銃制圧】による「1ラウンドに攻撃ロールを行えるのは分隊長を含め最大3名」という制限から、狙撃ポイントで待機しているスナイパーを除外する。

- 現場に同行している分隊長・戦闘員は、従来どおり合計最大3名まで攻撃ロールを行える。
- スナイパーは狙撃ポイントからの遠隔支援であるため、この3名枠を消費せず、屋外戦闘の参加条件を満たす限り別枠で通常どおり攻撃できる。
- スナイパーの第0ラウンド開始時射撃も従来どおり処理する。
- スポッターは攻撃能力を持たないため、この攻撃人数上限との直接の競合はない。
- この裁定は、狙撃ポイント待機要員を現場人数に含めないCore v1.01の位置関係と整合させる。

これにより、車載機銃の制圧は現場部隊の反撃人数を抑える一方、離れた狙撃ポイントからの射撃までは封じない。スナイパー編成には出目65で明確な戦術的価値が生まれるが、現場部隊への最大3名制限そのものは維持される。
"""
if heading not in a:
    a = a.rstrip() + section + "\n"
audit.write_text(a, encoding="utf-8")
