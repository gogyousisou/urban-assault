このPROJECT_CONTEXTを前提に相談します  
URBAN ASSAULTプロジェクトの続きです

# URBAN ASSAULT × ローグライクハーフ
Project Context

---

## Project Overview

URBAN ASSAULT × ローグライクハーフは、FT書房『ローグライクハーフ（RHL）』の基本ルールを基盤に、現代市街戦をテーマとして再構成した非公式バリアントです。

ジャンル：  
ソロTRPG / ローグライク / 戦術ゲーム

プレイ情報：
- プレイヤー人数：1～2人
- プレイ時間：15～30分（シナリオにより変動）
- 対象年齢：12歳以上
- GM：不要
- ジャンル：ミリタリー／現代戦／戦術
- レベル：初級
- 難易度：Normal
- 形式：サプリメント（バリアントルール）
- 世界：オリジナル（現実世界をベースにしたパラレルワールド）

特徴：
- 分隊戦術ゲーム
- 弾倉を中心とした資源管理
- 1シナリオ完結型
- ランダムイベント構造
- ソロプレイ前提、2人プレイ対応

---

## Repository

GitHub  
https://github.com/gogyousisou/urban-assault

公開リポジトリです。第三者著作物本文、公開許諾のない資料、秘密情報、APIキー等は格納しません。

---

## Branch Structure

### `main`
開発正本ブランチ。  
ルール改訂、シナリオ開発、研究メモ、テストプレイ資料などの開発成果を管理します。  
公開リポジトリであるため、開発途中であっても常に一般公開可能な内容だけを格納します。

### `public-release`
公開安定版ブランチ。  
一般利用者向けに確認済み・完成済みデータだけを格納します。  
`public-release` 側では直接開発を行いません。

### 公開フロー
`main → 内容確認 → public-release`

### 現在の改訂作業ブランチ
`refactor/v1.01-core-cleanup`

v1.01 の公開安全化、コアルール整合修正、リポジトリ整理を行う一時作業ブランチです。  
確認完了までは `main` / `public-release` へ直接反映しません。

---

## Version Status

- `refactor/v1.01-core-cleanup`：Core Rule v1.01 改訂候補
- `main`：Core Rule v1.00
- `public-release`：Core Rule v0.20（現行安定公開ブランチ）

v1.01 はまだ `main` / `public-release` へ反映していません。

---

## Core Rule Source of Truth

コアルールの唯一の正本：

`core/core-rule-full.md`

旧 `build/core-full.md` と自動コピー Workflow は P1 で廃止しました。  
現時点ではコアルールを複数ファイルへ分割しません。

---

## Scenario Structure

シナリオの正本テンプレート：

`docs/templates/scenario_template.md`

基本構造：

YAMLヘッダー  
↓  
シナリオ概要  
↓  
参加条件  
↓  
プロローグ  
↓  
特殊ルール  
↓  
マップ構造  
↓  
ランダムイベント  
↓  
中間イベント  
↓  
最終イベント  
↓  
エピローグ／リザルト

シナリオ格納：
- `scenarios/training/`：トレーニング
- `scenarios/missions/`：通常ミッション
- `scenarios/_dev/`：公開可能な開発途中シナリオ

---

## Publication / Copyright Policy

運用正本：

`docs/RLH_PUBLICATION_POLICY.md`

原則：
- ローグライクハーフ公式作品は設計研究の参考とする。
- URBAN ASSAULT の本文・シナリオ・データは独自文章・独自データを原則とする。
- d66 データの直接流用は原則として行わない。
- 公式作品本文や再配布を許可されていない第三者著作物はリポジトリに格納しない。
- 公開時は最新のローグライクハーフ制作利用規約を確認する。
- RLHロゴの現行正本は `images/RLH_icon.png`。

---

## v1.01 Completed Work

### P0 — Core cleanup / consistency
完了。

主な内容：
- 原作抜粋表記・原作文を URBAN ASSAULT 独自文章へ置換
- 作品情報を v1.01 へ更新
- 射撃・弾倉・行動単位を明確化
- 【スタングレネード】を定義
- 技能習得数を副能力値最大値基準へ統一
- 生命点 0 以下＝原則戦死へ統一
- 敵戦闘集団／高脅威目標の撤退条件を統一
- 敵攻撃配分、用語揺れ、戦利品、政治工作等を修正

判断記録：  
`docs/CORE_V1_01_P0_DECISIONS.md`

### P1 — Repository structure cleanup
完了。

主な内容：
- `core/core-rule-full.md` を唯一のコアルール正本へ統一
- `build/` と自動コピー Workflow を廃止
- `scenarios/misson/` → `scenarios/missions/` へ修正
- Black Sun Protocol のファイル名 typo を修正
- シナリオテンプレートを `docs/templates/scenario_template.md` へ統合
- テストプレイファイル名 typo を修正

判断記録：  
`docs/REPOSITORY_STRUCTURE_P1_DECISIONS.md`

---

## Current Development Focus

次工程は、v1.01 コアルールと既存シナリオ／設計資料の互換性監査です。

特に確認する項目：
- 既存シナリオの `core_version: 1.00` 表記
- 対象年齢 10～99歳など旧作品情報
- 分隊側の `逃走` → `退却`
- 敵側撤退条件と高脅威目標の扱い
- 弾倉消費・1ラウンド行動単位との整合
- 旧用語・旧章参照
- 公開安全性と独自文章方針

既存シナリオの内容変更は、ゲーム性に影響する場合はユーザー判断を得てから行います。

---

## Game Design Characteristics

- 分隊単位の戦術ゲーム
- 弾倉をリソースとする経済システム
- 1シナリオ完結型
- ローグライク構造
- 短時間プレイ
- 判断と資源管理が中心

---

## Future Plans

- v1.01 の `main` 反映
- 確認済み版の `public-release` 反映
- 既存シナリオ v1.01 対応
- 拡張ルール
- サプリメント
- 追加シナリオ
- Markdown → PDF 出版パイプライン
- 無料スターター冊子
- BOOTHでの有償版販売

---

## Development Environment

- iPhone中心の作業
- GitHubブラウザ運用
- Markdown編集
- VSCode使用
- インストール制限あり

---

## AI Assistance Expectations

- ゲームデザイン整理
- ルール整合性監査
- シナリオ制作補助
- GitHub運用支援
- 公開安全性チェック
- 出版パイプライン構築
- ドキュメント整備
