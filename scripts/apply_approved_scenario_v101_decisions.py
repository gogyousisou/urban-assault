from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected 1 match, found {count}")
    return text.replace(old, new, 1)


# Training scenario: make high-threat targets explicit.
training_path = Path("scenarios/training/d33_lvl10-11_tutorial_01_port.md")
training = training_path.read_text(encoding="utf-8")
training = replace_once(
    training,
    "- 専任伍長(レベル：4)",
    "- 専任伍長<高脅威目標>(レベル：4)",
    "training warrant officer high-threat label",
)
training = replace_once(
    training,
    "- 軽装甲制圧車両（レベル：5）",
    "- 軽装甲制圧車両<高脅威目標>（レベル：5）",
    "training suppression vehicle high-threat label",
)
training = replace_once(
    training,
    "- 軽装甲偵察車（レベル：5）  ",
    "- 軽装甲偵察車<高脅威目標>（レベル：5）  ",
    "training final vehicle high-threat label",
)
training_path.write_text(training, encoding="utf-8")


# Black Sun Protocol: apply all four approved compatibility decisions.
old_black_path = Path("scenarios/missions/d66_lvl10-16_mission_01_blacksun.md")
new_black_path = Path("scenarios/missions/d66_lvl12-16_mission_01_blacksun.md")
black = old_black_path.read_text(encoding="utf-8")
black = replace_once(
    black,
    "- recommended_level: 10-16",
    "- recommended_level: 12-16",
    "Black Sun recommended level",
)
black = replace_once(
    black,
    "効果は敵戦闘集団から1d6体の任意の敵を即時に倒します。1d6の範囲であれば異なる敵集団でも可能です。",
    "効果は敵戦闘集団から1d3+1体の任意の敵を即時に倒します。1d3+1の範囲であれば異なる敵集団でも可能です。",
    "Black Sun air support summary",
)
black = replace_once(
    black,
    "さらに、次に発生する戦闘では分隊員の攻撃参加上限を -2 する（最低1）。",
    "さらに、次に発生する戦闘では、各ラウンドに攻撃へ参加できる分隊員数の上限を、その戦闘開始時の生存戦闘員数 -2（最低1）とする。分隊長はこの上限に含めない。",
    "Black Sun vehicle IED attack limit",
)

if new_black_path.exists():
    raise SystemExit(f"target already exists: {new_black_path}")
new_black_path.write_text(black, encoding="utf-8")
old_black_path.unlink()
