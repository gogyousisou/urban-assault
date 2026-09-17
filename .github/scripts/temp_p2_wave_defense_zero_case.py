from pathlib import Path

scenario = Path("scenarios/missions/d66_lvl10-16_mission_01_blacksun.md")
s = scenario.read_text(encoding="utf-8")
old = "【1-2名：+0】【3-5名：+1】【6以上：+2】"
new = "【0-2名：+0】【3-5名：+1】【6以上：+2】"
if s.count(old) != 1:
    raise SystemExit(f"organized defense range marker count must be 1, got {s.count(old)}")
scenario.write_text(s.replace(old, new, 1), encoding="utf-8")

audit = Path("docs/SCENARIO_V1_01_RESOURCE_BALANCE_AUDIT.md")
a = audit.read_text(encoding="utf-8")
old_a = "- 防御ロール修正値は既存どおり【1-2名：+0】【3-5名：+1】【6以上：+2】とし、数値自体は変更しない。"
new_a = "- Core v1.01では戦闘員0名の編成も可能なため、0名時を既存の無補正帯に含め、【0-2名：+0】【3-5名：+1】【6以上：+2】とする。1名以上の既存補正値は変更しない。"
if a.count(old_a) != 1:
    raise SystemExit(f"audit organized defense range marker count must be 1, got {a.count(old_a)}")
a = a.replace(old_a, new_a, 1)
audit.write_text(a, encoding="utf-8")
