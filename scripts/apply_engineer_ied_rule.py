from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected 1 match, found {count}")
    return text.replace(old, new, 1)

core_path = Path("core/core-rule-full.md")
text = core_path.read_text(encoding="utf-8")
old = ">トラップ解除判定に +1  \n>IED(即席爆弾)により、1作戦につき1回、車両1体に1ダメージを与えます（防御ロール不可）。  "
new = ">トラップ解除判定に +1  \n>IED(即席爆弾)：1作戦につき1回、戦闘中に使用できます。対象は「車両」または「装甲」属性を持つ高脅威目標1体です。第0ラウンドでは使用できません。使用したラウンドはコンバットエンジニア自身の攻撃の代わりにこの能力を使用し、判定は行いません。弾倉を消費せず、対象に1ダメージを与えます（防御ロール不可）。  "
text = replace_once(text, old, new, "engineer IED rule")
core_path.write_text(text, encoding="utf-8")

audit_path = Path("docs/SCENARIO_V1_01_RESOURCE_BALANCE_AUDIT.md")
audit = audit_path.read_text(encoding="utf-8")naudit = audit.replace("ただし、コンバットエンジニアの対車両IED能力は使用タイミングと行動消費が未定義のため、上記計算には含めていません。", "コンバットエンジニアのIED能力は、承認済み仕様（1作戦1回・通常ラウンドで自身の攻撃の代わり・判定不要・弾倉消費なし・車両／装甲属性の高脅威目標へ1ダメージ）として扱います。")
marker = "## 9. テストを止めている次のルール判断"
if marker not in audit:
    raise SystemExit("audit marker not found")
head = audit.split(marker, 1)[0].rstrip()
new_section = """

## 9. コンバットエンジニアIED — 採用済み

ユーザー承認により、以下で確定します。

- 1作戦につき1回。
- 対象は「車両」または「装甲」属性を持つ高脅威目標1体。
- 第0ラウンドでは使用できない。
- 通常ラウンドでコンバットエンジニア自身の攻撃の代わりに使用する。
- 判定不要。
- 弾倉消費なし。
- 対象に1ダメージを与え、防御ロールは行わない。

以後の資源収支・難易度テストでは、この仕様を有効にして評価します。
"""
audit_path.write_text(head + new_section, encoding="utf-8")
