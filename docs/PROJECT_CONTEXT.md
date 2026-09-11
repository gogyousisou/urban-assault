このPROJECT_CONTEXTを前提に相談します
URBAN ASSAULTプロジェクトの続きです

# URBAN ASSAULT × ローグライクハーフ
Project Context

---

## Project Overview

URBAN ASSAULT × ローグライクハーフは  
「ローグライクハーフ（RHL）」の基本ルールをベースに  
現代市街戦をテーマとして再構成したバリアントTRPGです。

ジャンル：  
ソロTRPG / ローグライク / 戦術ゲーム

プレイ時間：  
約15〜30分

特徴：

・分隊戦術ゲーム  
・弾倉を中心とした資源管理  
・1シナリオ完結型  
・ランダムイベント構造  
・ソロプレイ前提  

---

## Repository

GitHub

https://github.com/gogyousisou/urban-assault

---

## Branch Structure

main  
開発正本ブランチ。  
ルール改訂、シナリオ開発、研究メモ、テストプレイ資料などの開発成果を管理する。  
ただし本リポジトリは公開リポジトリであるため、main に格納する内容は常に一般公開可能なものに限る。  
第三者の著作物本文、公開許諾のない資料、秘密情報、APIキー等を格納しない。  
開発途中の内容であっても、公開されることを前提として管理する。

public-release  
公開安定版ブランチ。  
一般利用者向けに公開する、確認済み・完成済みのデータのみを格納する。  
main で開発・確認を行い、公開可能と判断した版だけを public-release に反映する。

公開フロー  
main → 内容確認 → public-release

運用原則  
- main を開発上の正本とする。  
- public-release は配布・参照用の安定版とする。  
- public-release 側で直接開発を行わない。  
- main と public-release のどちらにも、再配布を許可されていない第三者著作物本文を格納しない。  
- ローグライクハーフ公式作品は設計研究の参考とし、URBAN ASSAULT側では独自文章・独自データを原則とする。

---

## Current Release

公開安定版：Core Rule v1.00  
公開内容：

・コアルール  
・ミニシナリオ2本  

---

## Current Development

開発版：Core Rule v1.01  
作業ブランチ：`refactor/v1.01-core-cleanup`

v1.01 P0整合修正は完了。  
主な反映内容：

・原作抜粋表記／原作文の独自文章化  
・公開用作品情報の整理  
・戦闘行動単位と弾倉消費の明確化  
・スタングレネードの定義  
・生命点0以下＝原則戦死への統一  
・敵撤退条件の統一  
・政治工作の端数処理修正  
・用語揺れ／参照／目次の整理  

判断記録：`docs/CORE_V1_01_P0_DECISIONS.md`

次工程は P1「GitHub内の構成整理・正本管理方法の整理」。

---

## Scenario Structure

URBAN ASSAULTのシナリオは以下の構造で制作される

YAMLヘッダー  
↓  
シナリオ概要  
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
エピローグ

---

## Game Design Characteristics

ゲーム設計の特徴

・分隊単位の戦術ゲーム  
・弾倉をリソースとする経済システム  
・1シナリオ完結型  
・ローグライク構造  
・短時間プレイ  
・判断と資源管理が中心  

---

## Current Development Focus

現在進めている作業

・コアルール v1.01 の整理  
・GitHub構成整理  
・シナリオフォーマット整理  
・GitHub公開運用  
・Markdown → PDF出版研究  
・Mermaid図の導入  
・無料スターター冊子制作  

---

## Future Plans

将来的な計画

・拡張ルール  
・サプリメント  
・追加シナリオ  
・BOOTHでの有償版販売  
・豪華組版PDF制作  

---

## Development Environment

制作環境

・iPhone中心の作業  
・GitHubブラウザ運用  
・Markdown編集  
・VSCode使用  
・インストール制限あり  

---

## AI Assistance Expectations

AIに期待するサポート

・ゲームデザイン整理  
・シナリオ制作補助  
・GitHub運用アドバイス  
・出版パイプライン構築  
・ドキュメント整備  
