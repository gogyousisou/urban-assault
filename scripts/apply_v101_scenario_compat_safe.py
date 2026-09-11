from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected 1 match, found {count}")
    return text.replace(old, new, 1)


def patch_training() -> None:
    path = Path("scenarios/training/d33_lvl10-11_tutorial_01_port.md")
    text = path.read_text(encoding="utf-8")

    text = replace_once(text, "core_version: 1.00", "core_version: 1.01", "training core version")
    text = replace_once(text, "- 対象年齢：10-99歳", "- 対象年齢：12歳以上", "training age")
    text = replace_once(
        text,
        "章立ては原作の基本ルールと同じですので、内容がわからない場合は原作の同章を参照してください。  ",
        "URBAN ASSAULT のコアルールと本シナリオの記載が異なる場合は、本シナリオの固有ルールを優先してください。  ",
        "training obsolete chapter guidance",
    )
    if text.count("【逃走】") != 2:
        raise SystemExit(f"training retreat term: expected 2 matches, found {text.count('【逃走】')}")
    text = text.replace("【逃走】", "【退却】")
    text = replace_once(text, "### ■ 逃走について", "### ■ 退却について", "training retreat heading")

    mechanic_count = text.count("コンバットメカニック")
    if mechanic_count != 2:
        raise SystemExit(f"training engineer term: expected 2 matches, found {mechanic_count}")
    text = text.replace("コンバットメカニック", "コンバットエンジニア")

    path.write_text(text, encoding="utf-8")


def patch_blacksun() -> None:
    path = Path("scenarios/missions/d66_lvl10-16_mission_01_blacksun.md")
    text = path.read_text(encoding="utf-8")

    text = replace_once(text, "- core_version: 1.00", "- core_version: 1.01", "blacksun core version")
    text = replace_once(text, "- scenario_id: d66-misson-01", "- scenario_id: d66-mission-01", "blacksun scenario id")
    text = replace_once(text, "- 対象年齢：10-99歳", "- 対象年齢：12歳以上", "blacksun age")
    text = replace_once(
        text,
        "章立ては原作の基本ルールと同じですので、内容がわからない場合は原作の同章を参照してください。",
        "URBAN ASSAULT のコアルールと本シナリオの記載が異なる場合は、本シナリオの固有ルールを優先してください。",
        "blacksun obsolete chapter guidance",
    )

    logo_anchor = "> https://ftbooks.booth.pm/items/4671946\n"
    if text.count(logo_anchor) != 1:
        raise SystemExit(f"blacksun logo anchor: expected 1 match, found {text.count(logo_anchor)}")
    logo = logo_anchor + "\n<p align=\"center\">\n  <img src=\"../../images/RLH_icon.png\" width=\"180\" alt=\"ローグライクハーフ ロゴ\">\n</p>\n"
    text = text.replace(logo_anchor, logo, 1)

    text = replace_once(text, "各章で「〇週目」と書かれた箇所", "各章で「〇周目」と書かれた箇所", "blacksun lap typo")
    text = replace_once(text, "- 2週目以降は分隊編成でDボーイズが編成できる。", "- 2周目以降は分隊編成でDボーイズが編成できる。", "blacksun second lap typo")
    text = replace_once(text, "技能：1 生命：1 射撃回数：1", "技量点：1 生命点：1 射撃回数：1", "blacksun d-boys stats")

    text = replace_once(text, "- 一本道モードにおける逃走", "- 一本道モードにおける退却", "blacksun retreat heading")
    text = replace_once(text, "基本ルールの「42：逃走」", "基本ルールの「42. 退却」", "blacksun chapter 42")
    text = replace_once(text, "ただし、中間イベントおよび最終イベントでは、逃走を行うことはできない。", "ただし、中間イベントおよび最終イベントでは、退却を行うことはできない。", "blacksun retreat prohibition")

    dup = "  33：<交差する車列>\n  33：<現地の案内人>\n  34：<現地の案内人>"
    fixed = "  33：<交差する車列>\n  34：<現地の案内人>"
    text = replace_once(text, dup, fixed, "blacksun duplicate d66 index")

    text = replace_once(text, "最終イベントクリアまたは分隊長死亡を指します。", "最終イベントクリアまたは分隊長戦死を指します。", "blacksun death term intro")
    text = replace_once(text, "分隊長が死亡した場合、その時点で作戦は失敗として終了する。", "分隊長が戦死した場合、その時点で作戦は失敗として終了する。", "blacksun death term result")

    path.write_text(text, encoding="utf-8")


patch_training()
patch_blacksun()
