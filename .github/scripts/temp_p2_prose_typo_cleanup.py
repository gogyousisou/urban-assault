from pathlib import Path

scenario = Path("scenarios/missions/d66_lvl10-16_mission_01_blacksun.md")
s = scenario.read_text(encoding="utf-8")
repls = {
    "民兵は集まりけれておらず、散発的な発砲だ。": "民兵は集まりきれておらず、散発的な発砲だ。",
    "簡単に突破する事出そうにない。": "簡単に突破することができそうにない。",
    "車両舞台の隊長の怒声": "車両部隊の隊長の怒声",
    "近ずけずにいるようだ。": "近づけずにいるようだ。",
}
for old, new in repls.items():
    if s.count(old) != 1:
        raise SystemExit(f"expected exactly one occurrence of {old!r}, got {s.count(old)}")
    s = s.replace(old, new, 1)
scenario.write_text(s, encoding="utf-8")

audit = Path("docs/SCENARIO_V1_01_RESOURCE_BALANCE_AUDIT.md")
a = audit.read_text(encoding="utf-8")
heading = "## 40. Black Sun 文章誤記の整理 — 非ゲームプレイ変更"
section = """

## 40. Black Sun 文章誤記の整理 — 非ゲームプレイ変更

追加監査で確認した明白な誤記を、ルール・数値・処理を変更せず修正した。

- 「民兵は集まりけれておらず」→「民兵は集まりきれておらず」
- 「簡単に突破する事出そうにない」→「簡単に突破することができそうにない」
- 「車両舞台の隊長」→「車両部隊の隊長」
- 「近ずけず」→「近づけず」

いずれも文章上の修正のみで、ゲームプレイへの影響はない。
"""
if heading not in a:
    audit.write_text(a.rstrip() + section + "\n", encoding="utf-8")
