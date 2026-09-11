# URBAN ASSAULT v1.01 — P1 GitHub構成整理 判断事項

対象ブランチ：`refactor/v1.01-core-cleanup`

P0整合修正完了後のリポジトリ構成を確認し、今後の正本管理を単純化するための判断事項をまとめます。

## 1. コアルール正本と `build/` — 判断必要

現在は以下が併存しています。

- 正本：`core/core-rule-full.md`
- 複製：`build/core-full.md`
- 自動コピー：`.github/workflows/main.yml`

現状の `build/core-full.md` は旧版のままで、v1.01 の `core/core-rule-full.md` と一致していません。
GitHub Actions の `GITHUB_TOKEN` で作成したコミットは別ワークフローを再起動しないため、更新経路によっては `build/` が追従しない状態が発生します。

### 推奨案

`core/core-rule-full.md` を唯一のコアルール正本として維持し、以下を削除する。

- `build/core-full.md`
- `.github/workflows/main.yml`

現時点ではコアルールを複数ファイルへ分割しない。
理由は、iPhone／GitHubブラウザ中心の運用と「正本を1ファイルに固定する」方針の方が、同期漏れや生成物との不一致を防ぎやすいため。

PDF等の生成物が必要になった時点で、GitHub上の正本を入力として出版用パイプラインを別途設計する。

## 2. シナリオディレクトリ名の誤記 — 推奨修正

現在：

- `scenarios/misson/`
- `d66_lvl10-16_misson_01_blacksun.md`

### 推奨案

以下へ名称を修正する。

- `scenarios/missions/`
- `d66_lvl10-16_mission_01_blacksun.md`

内容は変更せず、参照先がある場合は同時に更新する。

## 3. シナリオテンプレート重複 — 判断必要

現在、用途が重なる2つのテンプレートがあります。

- `docs/scenario_template.md`
- `docs/templates/scnario_template.md`（ファイル名に typo）

後者の方が詳細ですが、Core v1.00、対象年齢10～99歳、`逃走` 等の旧表記を含みます。

### 推奨案

`docs/templates/scenario_template.md` を唯一の正本テンプレートとする。

- 詳細版をベースに v1.01 へ更新。
- 対象年齢を12歳以上へ統一。
- `逃走` を分隊側の正式用語 `退却` へ統一。
- 公開用作品情報を最新ルールへ合わせる。
- `docs/scenario_template.md` と typo の `docs/templates/scnario_template.md` は統合後に削除。

## 4. テストプレイファイル名の typo — 推奨修正

現在：`testplay/tesr_chara_KURUTU_kiyou`

### 推奨案

内容を確認した上で、Markdownであれば拡張子を含む分かりやすい英数字名へ変更する。
例：`testplay/test_chara_kurutu_kiyou.md`

## 5. `scenarios/_dev/` の扱い — 現状維持を推奨

`main` は公開可能な開発正本とする方針が確定しているため、公開されても問題のない開発途中シナリオは `_dev/` に置いてよい。

非公開資料や第三者著作物本文を `_dev/` に置くことはしない。

## 6. コアルール表紙画像 — 現時点では削除しない

`core/assets/` には以下の3画像があります。

- `UAxRLH_core_cover_base.png`
- `UAxRLH_core_cover_ura_base_1.png`
- `UAxRLH_core_cover_ura_base_2.png`

どの版を今後使うかは見た目・出版方針に関わるため、P1では削除しない。
重複整理はPDF／スターター冊子の出版パイプライン設計時に判断する。

## P1でユーザー判断が必要な項目

1. `build/` と自動コピーWorkflowを廃止し、`core/core-rule-full.md` を唯一の正本にするか。
2. シナリオテンプレートを `docs/templates/scenario_template.md` 1本へ統合するか。

上記2点が承認された場合、ディレクトリ名・ファイル名の typo 修正を含めてP1整理を実施する。
