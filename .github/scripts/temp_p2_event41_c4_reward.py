from pathlib import Path

scenario = Path("scenarios/missions/d66_lvl10-16_mission_01_blacksun.md")
s = scenario.read_text(encoding="utf-8")
old = """- 爆弾の解除を試みる場合、器用ロールを振る(目標値：4)。分隊員にコンバットエンジニアがいる場合は器用ロールに+2の修正を与える。\n  - 解除成功：爆弾の材に使われていた弾薬を回収。弾倉1個を得る。\n  - 解除失敗：分隊長は直ちに1ダメージを受ける。加えて次の戦闘において、最初の1回のみ分隊長の防御ロールに-1の修正を与える。\n"""
new = """- 爆弾の解除を試みる場合、器用ロールを振る(目標値：4)。分隊員にコンバットエンジニアがいる場合は器用ロールに+2の修正を与える。\n  - 解除成功：爆弾の材に使われていた弾薬を回収。弾倉1個を得る。\n  - 解除失敗：分隊長は直ちに1ダメージを受ける。加えて次の戦闘において、最初の1回のみ分隊長の防御ロールに-1の修正を与える。\n- C4爆薬：Core v1.01の【C4爆薬】でこのIEDを自動解除することもできる。この場合は解除判定を行わず安全に通過できるが、【解除成功】による弾倉1個の回収は行わない。\n"""
if s.count(old) != 1:
    raise SystemExit(f"event41 block count must be 1, got {s.count(old)}")
scenario.write_text(s.replace(old, new, 1), encoding="utf-8")

audit = Path("docs/SCENARIO_V1_01_RESOURCE_BALANCE_AUDIT.md")
a = audit.read_text(encoding="utf-8")
heading = "## 39. Black Sun 出目41のC4自動解除と回収報酬 — 採用済み"
section = """

## 39. Black Sun 出目41のC4自動解除と回収報酬 — 採用済み

ユーザー承認により、出目41【薄暗い部屋】でCore v1.01の【C4爆薬】によるブービートラップ自動解除を使用した場合、解除成功時の弾倉回収報酬は得ない。

- 器用ロールで解除を試み、成功した場合は従来どおり弾倉1個を得る。
- C4爆薬を使用した場合は、Core v1.01の効果により判定不要で自動解除する。
- C4による自動解除では、出目41の【解除成功】に付随する弾倉1個の回収は行わない。
- したがって「判定リスクを負って解除し、成功すれば弾倉を回収する」か、「C4を消費して安全に解除する」かの選択となる。
- 出目41の工兵補正+2は前項どおり維持する。

これにより、C4の確実性と器用ロール解除の資源回収メリットを両立させる。
"""
if heading not in a:
    audit.write_text(a.rstrip() + section + "\n", encoding="utf-8")
