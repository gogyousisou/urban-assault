from pathlib import Path

scenario = Path("scenarios/missions/d66_lvl10-16_mission_01_blacksun.md")
text = scenario.read_text(encoding="utf-8")
old1 = """- <補給・資源>【十の位：1】
  11：<静まり返った路地>
  12：<放棄されたバックパック>
  13：<壊れた無線機>
  14：<崩れた建物の陰>
  15：<散乱した弾薬>
  16：<書きかけの地図>
"""
new1 = """- <補給・資源>【十の位：1】
  11：<放棄された補給箱>
  12：<避難民の集団>
  13：<壊れた無線機>
  14：<崩れた建物の陰>
  15：<はぐれたレンジャー>
  16：<書きかけの地図>
"""
old2 = """- <環境・状況圧力>【十の位：2】
  21：<避難民の集団>
  22：<負傷兵の救護>
  23：<補給トラック>
  24：<放棄された補給箱>
  25：<はぐれたレンジャー>
  26：<放棄された装備>
"""
new2 = """- <環境・状況圧力>【十の位：2】
  21：<民兵の検問>
  22：<屋上の見張り>
  23：<略奪する民兵>
  24：<死の商人>
  25：<離反した民兵>
  26：<扇動される民兵>
"""
for old,new,label in [(old1,new1,"11-16"),(old2,new2,"21-26")]:
    if text.count(old) != 1:
        raise SystemExit(f"{label} target count must be 1, got {text.count(old)}")
    text = text.replace(old,new,1)
scenario.write_text(text, encoding="utf-8")

audit = Path("docs/SCENARIO_V1_01_RESOURCE_BALANCE_AUDIT.md")
a = audit.read_text(encoding="utf-8")
section = """

## 16. Black Sun d66一覧と詳細見出しの同期 — 修正済み

d66一覧の11～26に、詳細本文と一致しない旧見出しが残っていたため、詳細本文の出目番号・イベント名を正として一覧だけを同期しました。

- 11～16：詳細本文の「放棄された補給箱／避難民の集団／壊れた無線機／崩れた建物の陰／はぐれたレンジャー／書きかけの地図」に統一。
- 21～26：詳細本文の「民兵の検問／屋上の見張り／略奪する民兵／死の商人／離反した民兵／扇動される民兵」に統一。
- イベント効果、出目番号、難易度、資源量は変更していない。

これは索引と詳細本文の不一致を解消する非ゲームプレイ変更です。
"""
heading = "## 16. Black Sun d66一覧と詳細見出しの同期 — 修正済み"
if heading not in a:
    audit.write_text(a.rstrip() + section + "\n", encoding="utf-8")
