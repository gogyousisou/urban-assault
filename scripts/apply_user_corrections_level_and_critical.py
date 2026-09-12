from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected 1 match, found {count}")
    return text.replace(old, new, 1)


# 1) Core v1.01: critical attacks chain as long as criticals continue.
core_path = Path("core/core-rule-full.md")
core = core_path.read_text(encoding="utf-8")
core = replace_once(
    core,
    "【攻撃ロール】でクリティカルが発生した場合、直ちに追加で【攻撃ロール】を1回行うことができる。  \nクリティカルによる追加攻撃では、弾倉を消費しない。",
    "【攻撃ロール】でクリティカルが発生した場合、直ちに追加で【攻撃ロール】を1回行うことができる。  \nこの追加攻撃でもクリティカルが発生した場合、さらに追加で【攻撃ロール】を1回行うことができる。この処理は、クリティカルが発生しなくなるまで繰り返す。  \nクリティカルによる追加攻撃では、弾倉を消費しない。",
    "core chained critical rule",
)
core_path.write_text(core, encoding="utf-8")


# 2) Black Sun Protocol: restore recommended level 10-16 everywhere.
old_path = Path("scenarios/missions/d66_lvl12-16_mission_01_blacksun.md")
new_path = Path("scenarios/missions/d66_lvl10-16_mission_01_blacksun.md")
if not old_path.exists():
    raise SystemExit(f"missing source: {old_path}")
if new_path.exists():
    raise SystemExit(f"target already exists: {new_path}")
black = old_path.read_text(encoding="utf-8")
black = replace_once(black, "- recommended_level: 12-16", "- recommended_level: 10-16", "Black Sun YAML recommended level")
black = replace_once(black, "経験点：12以上を想定しています。", "経験点：10以上を想定しています。", "Black Sun experience assumption")
black = replace_once(black, "- 適正レベル：12-16", "- 適正レベル：10-16", "Black Sun body recommended level")
new_path.write_text(black, encoding="utf-8")
old_path.unlink()


# 3) Compatibility audit: record the corrected recommended level and path.
compat_path = Path("docs/SCENARIO_V1_01_COMPATIBILITY_AUDIT.md")
compat = compat_path.read_text(encoding="utf-8")
compat = compat.replace("scenarios/missions/d66_lvl12-16_mission_01_blacksun.md", "scenarios/missions/d66_lvl10-16_mission_01_blacksun.md")
compat = replace_once(
    compat,
    "12～16 に統一しました。\n\n- ファイル名：`d66_lvl12-16_mission_01_blacksun.md`\n- YAML：`recommended_level: 12-16`\n- 本文：経験点12以上／適正レベル12-16",
    "ユーザー訂正により、推奨レベルは **10～16** に統一しました。\n\n- ファイル名：`d66_lvl10-16_mission_01_blacksun.md`\n- YAML：`recommended_level: 10-16`\n- 本文：経験点10以上／適正レベル10-16",
    "compat corrected recommended level block",
)
compat_path.write_text(compat, encoding="utf-8")


# 4) Resource-balance audit: update target path/level and lock chained criticals as an adopted rule.
resource_path = Path("docs/SCENARIO_V1_01_RESOURCE_BALANCE_AUDIT.md")
resource = resource_path.read_text(encoding="utf-8")
resource = resource.replace("scenarios/missions/d66_lvl12-16_mission_01_blacksun.md", "scenarios/missions/d66_lvl10-16_mission_01_blacksun.md")
resource = replace_once(resource, "推奨キャラクターレベルは12～16です。", "推奨キャラクターレベルは10～16です。", "resource recommended level")
resource = replace_once(resource, "ただし、レベル12～16の代表ビルドがまだ固定されておらず、", "ただし、レベル10～16の代表ビルドがまだ固定されておらず、", "resource representative builds")
resource = replace_once(
    resource,
    "- Black Sun Protocol：レベル12、14、16、NORMAL 28",
    "- Black Sun Protocol：レベル10、12、14、16、NORMAL 28",
    "resource Black Sun test levels",
)
old_section = """## 8. テスト開始前に残るルール解釈\n\nCore v1.01 の08章では、攻撃ロールでクリティカルした場合に無料の追加攻撃を行えるとしています。\n\nただし、**その追加攻撃でも再びクリティカルが出た場合、さらに追加攻撃が発生するか**は明示していません。\n\n資源収支テストを再現可能にするため、この点を先に固定する必要があります。\n\n### 推奨案\n\n**クリティカルによる追加攻撃は連鎖しない。**\n\n- 通常の攻撃ロールでクリティカル → 無料の追加攻撃を1回行う。\n- その無料追加攻撃で6が出ても、さらに追加攻撃は発生しない。\n- 1回の通常攻撃から発生する無料追加攻撃は最大1回。\n\n理由：\n\n- 1回の弾倉消費から得られる攻撃回数に上限ができ、資源収支を安定させられる。\n- 処理が簡単で、ソロプレイでも解釈が分かれにくい。\n- クリティカルの爽快感は残しつつ、極端な連鎖を防げる。\n\nこの点を確定後、同一条件で資源収支テストを実施します。"""
new_section = """## 8. クリティカル連鎖 — 採用済み\n\nユーザー判断により、**クリティカルによる追加攻撃は連鎖します。**\n\n- 通常の【攻撃ロール】でクリティカル → 無料の追加【攻撃ロール】を1回行う。\n- その追加攻撃でもクリティカルが発生した場合 → さらに無料の追加【攻撃ロール】を1回行う。\n- 以後、クリティカルが発生しなくなるまで同じ処理を繰り返す。\n- クリティカルによる追加攻撃では弾倉を追加消費しない。\n\nこの仕様は、低確率の幸運が連続するダイスゲームらしさを重視したものです。\n\n1回の有料攻撃から発生する攻撃ロール総数の期待値は、クリティカル率を1/6とすると `1 / (1 - 1/6) = 1.2回` です。したがって平均値への影響は限定的ですが、まれに大きな連鎖が起こる分散の大きい仕様として扱います。\n\n資源収支テストでは、この連鎖を有効にした状態で判定します。"""
if old_section not in resource:
    raise SystemExit("resource critical section: expected exact block not found")
resource = resource.replace(old_section, new_section, 1)
resource_path.write_text(resource, encoding="utf-8")
