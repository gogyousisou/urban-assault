from pathlib import Path

core = Path("core/core-rule-full.md")
s = core.read_text(encoding="utf-8")
old = """- 被弾テーブル  \n  1d6を振り、出目に対応する役割の戦闘員がダメージを受けます。  \n"""
new = """- 被弾テーブル  \n  【被弾ロール】を行う時点で対象となれる戦闘員が1名もいない場合、ロールは行わず分隊長を対象とします。シナリオに別の対象指定がある場合は、その記載を優先します。  \n  対象となれる戦闘員が1名以上いる場合は1d6を振り、出目に対応する役割の戦闘員がダメージを受けます。  \n"""
if s.count(old) != 1:
    raise SystemExit(f"Core hit-table marker count must be 1, got {s.count(old)}")
core.write_text(s.replace(old, new, 1), encoding="utf-8")

audit = Path("docs/SCENARIO_V1_01_RESOURCE_BALANCE_AUDIT.md")
a = audit.read_text(encoding="utf-8")
heading = "## 28. Core 被弾ロール対象0名時の共通フォールバック — 採用済み"
section = """

## 28. Core 被弾ロール対象0名時の共通フォールバック — 採用済み

ユーザー承認により、Core v1.01の【被弾テーブル】に、対象となれる戦闘員が0名の場合の共通処理を追加する。

- 【被弾ロール】を行う時点で対象となれる戦闘員が1名もいない場合、ロールは行わず分隊長を対象とする。
- シナリオに別の対象指定がある場合は、そのシナリオ記載を優先する。
- 対象となれる戦闘員が1名以上いる場合は、従来どおり1d6の【被弾ロール】で役割を決定する。
- 非戦闘員および狙撃ポイント待機中の隊員は、特記がない限り従来どおり被弾テーブルの対象外とする。
- Black Sun 出目42の個別フォールバックは、このCore共通規定と同内容の明示として残す。
- Black Sun 出目43【遠隔起爆】、出目46【車両IED】など、直接【被弾ロール】を指示するイベントにもこの共通規定を適用する。

これにより、戦闘員を編成していない分隊や、戦闘員が全員脱落した状態でも【被弾ロール】を含むイベント処理が停止しない。
"""
if heading not in a:
    audit.write_text(a.rstrip() + section + "\n", encoding="utf-8")
