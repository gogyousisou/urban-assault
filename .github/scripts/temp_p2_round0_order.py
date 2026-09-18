from pathlib import Path

core = Path("core/core-rule-full.md")
c = core.read_text(encoding="utf-8")
old = """を行うことができます。

スナイパーの開始時射撃は、参加可能なスナイパー自身が通常の先攻順より前に1回だけ行う攻撃です。分隊全体の先攻は変更せず、第1ラウンド以降の行動順にも影響しません。  
"""
new = """を行うことができます。

第0ラウンドで使用できる分隊側の効果が複数ある場合、プレイヤーが任意の順番を選び、1つずつ効果を最後まで処理してから次の効果を使用します。途中で戦闘状況が変化した場合、以後の効果は変化後の状況を参照します。シナリオや個別の装備・技能に処理順が明記されている場合は、その記載を優先します。

スナイパーの開始時射撃は、参加可能なスナイパー自身が通常の先攻順より前に1回だけ行う攻撃です。分隊全体の先攻は変更せず、第1ラウンド以降の行動順にも影響しません。  
"""
if c.count(old) != 1:
    raise SystemExit(f"core anchor count={c.count(old)}")
c = c.replace(old, new, 1)
core.write_text(c, encoding="utf-8")

scenario = Path("scenarios/missions/d66_lvl10-16_mission_01_blacksun.md")
s = scenario.read_text(encoding="utf-8")
old = "  各攻撃ロールの前に、地上または屋上の民兵のいずれを対象にするか指定すること。"
new = "  各攻撃ロールの前に、地上または4階の民兵のいずれを対象にするか指定すること。"
if s.count(old) != 1:
    raise SystemExit(f"scenario anchor count={s.count(old)}")
s = s.replace(old, new, 1)
scenario.write_text(s, encoding="utf-8")

decisions = Path("docs/CORE_V1_01_P0_DECISIONS.md")
d = decisions.read_text(encoding="utf-8")
heading = "## 17. 第0ラウンドの複数効果の処理順 — 承認・反映済み"
section = """

## 17. 第0ラウンドの複数効果の処理順 — 承認・反映済み

ユーザー判断により、第0ラウンドで使用可能な分隊側の効果が複数ある場合の処理順を次のように整理する。

- スナイパーの開始時射撃、消耗装備、一部スキルなど、第0ラウンドで使用可能な分隊側の効果はプレイヤーが任意の順番で処理できる。
- 1つの効果を最後まで処理してから次の効果へ進む。
- 先の効果によって敵人数・生命点・状態などが変化した場合、後続の効果は変化後の戦闘状況を参照する。
- シナリオ、装備、技能などに明示的な処理順が記載されている場合は、その個別記載を優先する。
- 第0ラウンドで直接ダメージを与える技能を使用できない既存制限など、各効果固有の使用条件は変更しない。

これにより、第0ラウンドに複数の選択肢が重なった場合でも固定順を追加せず、プレイヤーが状況に応じて投入順を判断できる。
"""
if heading not in d:
    d = d.rstrip() + section + "\n"
decisions.write_text(d, encoding="utf-8")

audit = Path("docs/SCENARIO_V1_01_RESOURCE_BALANCE_AUDIT.md")
a = audit.read_text(encoding="utf-8")
heading = "## 60. 第0ラウンドの任意処理順とBlack Sun 2周目中間イベント — 採用済み"
section = """

## 60. 第0ラウンドの任意処理順とBlack Sun 2周目中間イベント — 採用済み

ユーザー承認により、Core v1.01へ「第0ラウンドで使用可能な分隊側の効果は、特記がない限りプレイヤーが任意の順番で1つずつ処理する」という共通規定を追加する。

- Black Sun 2周目中間イベントでは、第0ラウンドにフラググレネードを使用でき、スナイパーが参加可能な場合は開始時射撃も使用できる。
- 両方を使用する場合、プレイヤーはフラググレネードとスナイパー開始時射撃のどちらを先に処理するか選べる。
- 先に処理した効果で民兵が脱落した場合、後続の効果は減少後の敵配置を参照する。
- 同イベントの攻撃対象指定に残っていた「地上または屋上」は、敵配置が「4階（属性：室内）」であることに合わせ、「地上または4階」へ整合修正する。これは対象や難易度を変更する新規ルールではない。

この整理により、第0ラウンドの複数効果を将来追加しても個別の固定順を増やさず処理でき、Black Sunのフラググレネードとスナイパーの組み合わせにも明確な戦術選択が生まれる。
"""
if heading not in a:
    a = a.rstrip() + section + "\n"
audit.write_text(a, encoding="utf-8")
