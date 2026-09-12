from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected 1 match, found {count}")
    return text.replace(old, new, 1)

scenario_path = Path("scenarios/missions/d66_lvl10-16_mission_01_blacksun.md")
scenario = scenario_path.read_text(encoding="utf-8")
old = """### 2周目

_墜落地点南東に陣取ったチョーク4は周辺を固め防御陣地を構築した。_
_やがて、他のレンジャーやDボーイズ達が到着し、それぞれが現場の確保に努めている。_
_民兵の狂気をはらんだ奇声と銃声は、一時的になりを潜めている。_
_戦場に訪れる、束の間の静寂。_
_「国連と第10山岳師団による救出部隊の編成が完了した！もう少しだ、踏ん張れ！」_
_再び隊員達の目に、希望と闘志の灯がともる。_
_だが... 今まで静かだった夜の空気に、民兵の奇声と足音が混じり始める。_
_どうやら救出部隊の出動を察知した民兵たちが、こちらに押し寄せてきているようだ。_

---

**属性：屋外・夜間**

- 民兵 6 + 1d3 名[地上]
- レベル：5
- 2ラウンド目以降、ラウンド開始時に民兵 2 + 1d3 名[地上]が追加される。
"""
new = """### 2周目

_墜落地点南東に陣取ったチョーク4は周辺を固め防御陣地を構築した。_
_やがて、他のレンジャーやDボーイズ達が到着し、それぞれが現場の確保に努めている。_
_民兵の狂気をはらんだ奇声と銃声は、一時的になりを潜めている。_
_戦場に訪れる、束の間の静寂。_
_「国連と第10山岳師団による救出部隊の編成が完了した！もう少しだ、踏ん張れ！」_
_再び隊員達の目に、希望と闘志の灯がともる。_
_だが... 今まで静かだった夜の空気に、民兵の奇声と足音が混じり始める。_
_どうやら救出部隊の出動を察知した民兵たちが、こちらに押し寄せてきているようだ。_

---

**属性：屋外・夜間**

- 民兵 6 + 1d3 名[地上]
- レベル：5
- 反応：死ぬまで戦う
- 2ラウンド目以降、ラウンド開始時に民兵 2 + 1d3 名[地上]が追加される。
"""
scenario = replace_once(scenario, old, new, "Black Sun round 2 final reaction")
scenario_path.write_text(scenario, encoding="utf-8")

audit_path = Path("docs/SCENARIO_V1_01_RESOURCE_BALANCE_AUDIT.md")
audit = audit_path.read_text(encoding="utf-8").rstrip()
section = """

## 10. Black Sun 2周目最終イベントの反応 — 採用済み

ユーザー承認により、2周目最終イベントの民兵は【死ぬまで戦う】として扱います。

- 敵戦闘集団の「初期人数の半分以下で自動撤退」は適用しない。
- 2ラウンド目以降の増援は予定どおり発生する。
- 3ラウンド終了後、シナリオ固有条件として救出部隊が到着し戦闘終了する。

これにより、同イベントは3ラウンド耐久戦として資源収支・難易度テストを行います。
"""
if "## 10. Black Sun 2周目最終イベントの反応 — 採用済み" in audit:
    raise SystemExit("audit section already exists")
audit_path.write_text(audit + section, encoding="utf-8")
