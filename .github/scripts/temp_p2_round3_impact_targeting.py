from pathlib import Path

scenario = Path("scenarios/missions/d66_lvl10-16_mission_01_blacksun.md")
text = scenario.read_text(encoding="utf-8")
old = """  - 対戦車砲は奇数ラウンドのみ発射する。\n    - 防御ロールに失敗した際、奇数なら分隊長が、偶数なら分隊員が被弾する。\n    - 防御ロールの出目が1(ファンブル)の場合は２ダメージ受ける。\n"""
new = """  - 対戦車砲は奇数ラウンドのみ発射する。\n    - 対戦車砲が攻撃するたび、防御ロールの前に【着弾対象ロール】として1d6を振る。奇数なら分隊長、偶数なら分隊員側を攻撃対象とする。\n    - 分隊員側が対象となった場合、通常どおり防御ロールを行い、防御に失敗したら【被弾ロール】で実際に被弾する隊員を決定する。攻撃対象となれる分隊員が1名もいない場合は、分隊長を対象とする。\n    - 対象確定後、その対象について通常どおり防御ロールを行う。防御ロールの出目が1(ファンブル)の場合は2ダメージを受ける。\n"""
if text.count(old) != 1:
    raise SystemExit(f"target count must be 1, got {text.count(old)}")
scenario.write_text(text.replace(old, new, 1), encoding="utf-8")

audit = Path("docs/SCENARIO_V1_01_RESOURCE_BALANCE_AUDIT.md")
a = audit.read_text(encoding="utf-8")
section = """

## 15. Black Sun 3周目最終戦の着弾対象ロール — 採用済み

ユーザー承認により、3周目最終戦の対戦車砲は、防御ロールより前に【着弾対象ロール】を行って攻撃対象を決定します。

- 対戦車砲は奇数ラウンドのみ攻撃する。
- 攻撃ごとに、防御ロール前に1d6の【着弾対象ロール】を行う。
- 奇数なら分隊長、偶数なら分隊員側を攻撃対象とする。
- 分隊員側が対象となった場合、防御に失敗した後で【被弾ロール】を行い、実際に被弾する隊員を決定する。
- 攻撃対象となれる分隊員がいない場合は分隊長を対象とする。
- 対象確定後、その対象について通常どおり防御ロールを行う。
- 防御ロールの出目が1（ファンブル）の場合は、既存仕様どおり2ダメージを受ける。

これにより、着弾位置のランダム性を残しつつ、分隊長の防護装備修正と分隊員側の防御処理をCore v1.01の手順どおり適用できます。
"""
heading = "## 15. Black Sun 3周目最終戦の着弾対象ロール — 採用済み"
if heading not in a:
    audit.write_text(a.rstrip() + section + "\n", encoding="utf-8")
