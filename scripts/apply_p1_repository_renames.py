from pathlib import Path


def move(src: str, dst: str) -> None:
    source = Path(src)
    target = Path(dst)
    if not source.exists():
        raise SystemExit(f"missing source: {src}")
    if target.exists():
        raise SystemExit(f"target already exists: {dst}")
    target.parent.mkdir(parents=True, exist_ok=True)
    source.rename(target)


move(
    "scenarios/misson/d66_lvl10-16_misson_01_blacksun.md",
    "scenarios/missions/d66_lvl10-16_mission_01_blacksun.md",
)

# Remove the now-empty typo directory if it still exists.
old_dir = Path("scenarios/misson")
if old_dir.exists():
    old_dir.rmdir()

move(
    "testplay/tesr_chara_KURUTU_kiyou",
    "testplay/test_chara_kurutu_kiyou.md",
)
