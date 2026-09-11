# URBAN ASSAULT v1.01 — P1 GitHub構成整理

対象ブランチ：`refactor/v1.01-core-cleanup`

P0整合修正後のリポジトリ構成を整理し、正本管理と公開運用を単純化するための判断・実施記録です。

## 1. コアルール正本 — 承認・反映済み

`core/core-rule-full.md` を唯一のコアルール正本とします。

削除済み：

- `build/core-full.md`
- `.github/workflows/main.yml`

`build/` の複製と自動コピーを廃止し、正本と生成物の不一致が起きない構成へ変更しました。  
現時点ではコアルールを複数ファイルへ分割しません。

PDF 等の生成物が必要になった時点で、`core/core-rule-full.md` を入力とする出版用パイプラインを別途設計します。

## 2. シナリオディレクトリ名 — 反映済み

旧：

- `scenarios/misson/`
- `d66_lvl10-16_misson_01_blacksun.md`

新：

- `scenarios/missions/`
- `d66_lvl10-16_mission_01_blacksun.md`

内容は変更せず、ファイル名とディレクトリ名の typo のみ修正しました。

## 3. シナリオテンプレート — 承認・反映済み

唯一の正本テンプレートを次へ統一しました。

- `docs/templates/scenario_template.md`

反映内容：

- Core v1.01 対応
- 対象年齢 12 歳以上
- 分隊側【退却】／敵側【撤退】へ用語統一
- 高脅威目標の撤退条件記入欄を追加
- RLH 基本ルール・利用規約の参照先を明記
- 公開用作品情報を現行方針へ更新
- 制作時チェック項目を追加

削除済み：

- `docs/scenario_template.md`
- `docs/templates/scnario_template.md`

## 4. テストプレイファイル名 — 反映済み

旧：

- `testplay/tesr_chara_KURUTU_kiyou`

新：

- `testplay/test_chara_kurutu_kiyou.md`

内容は変更せず、ファイル名と拡張子のみ整理しました。

## 5. `scenarios/_dev/` — 現状維持

公開されても問題のない開発途中シナリオは `_dev/` に置いて構いません。  
非公開資料、第三者著作物本文、秘密情報は格納しません。

## 6. コアルール表紙画像 — 現状維持

`core/assets/` の表紙画像 3 点は P1 では削除しません。  
出版パイプライン設計時に採用版を決定します。

## P1完了条件

以下を確認済みです。

- コアルール正本は `core/core-rule-full.md` の 1 本のみ。
- `build/` と自動コピー Workflow は現行ツリーから削除済み。
- `scenarios/missions/` へ名称修正済み。
- シナリオテンプレートは `docs/templates/scenario_template.md` の 1 本へ統合済み。
- テストプレイファイル名の typo を修正済み。
- 一時的な移行用 Workflow／Script は削除済み。

P1 GitHub構成整理は完了とします。
