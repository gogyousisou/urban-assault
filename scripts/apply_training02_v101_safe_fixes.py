from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected 1 match, found {count}")
    return text.replace(old, new, 1)


def insert_training_level(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    marker = "- 対象年齢：12歳以上  \n- 難易度：NORMAL"
    replacement = "- 対象年齢：12歳以上  \n- レベル：初級  \n- 難易度：NORMAL"
    text = replace_once(text, marker, replacement, f"{path} TOS level")
    path.write_text(text, encoding="utf-8")


# Training 01: add the missing TOS publication level only.
insert_training_level(Path("scenarios/training/d33_lvl10-11_tutorial_01_port.md"))

# Training 02: bring non-gameplay wording/metadata in line with v1.01.
path = Path("scenarios/training/d33_lvl10-11_tutorial_02_contact.md")
text = path.read_text(encoding="utf-8")
text = replace_once(text, "core_version: 1.00", "core_version: 1.01", "training02 core version")
text = replace_once(text, "- 対象年齢：10-99歳  \n- 難易度：NORMAL", "- 対象年齢：12歳以上  \n- レベル：初級  \n- 難易度：NORMAL", "training02 publication metadata")
text = replace_once(
    text,
    "章立ては原作の基本ルールと同じですので、内容がわからない場合は原作の同章を参照してください。  ",
    "URBAN ASSAULT のコアルールと本シナリオの記載が異なる場合は、本シナリオの固有ルールを優先してください。  ",
    "training02 precedence wording",
)
text = replace_once(text, "## ■ シナリオ特殊ルール（交戦規定）", "## 05. シナリオ特殊ルール（交戦規定）", "training02 section number")
text = replace_once(text, "### ■ 逃走について", "### ■ 退却について", "training02 retreat heading")
text = text.replace("【逃走】", "【退却】")
text = replace_once(text, "分隊の撤退は【指揮ロール】で行う。", "分隊の退却は【指揮ロール】で行う。", "training02 player retreat terminology")
text = replace_once(text, '<img src="../../images/RLH_icon.png" width="180">', '<img src="../../images/RLH_icon.png" width="180" alt="ローグライクハーフ ロゴ">', "training02 logo alt")
path.write_text(text, encoding="utf-8")
