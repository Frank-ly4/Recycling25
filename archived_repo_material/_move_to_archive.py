import os, shutil
from pathlib import Path

root = Path('.')
archive = root / 'archived_repo_material'
archive.mkdir(exist_ok=True)

keep = {
    'business_plan_rebuild',
    'archived_repo_material',
    '.git',
    '.cursor',
}

for p in root.iterdir():
    name = p.name
    if name in keep:
        continue
    dest = archive / name
    if dest.exists():
        # avoid overwriting
        continue
    shutil.move(str(p), str(dest))

print('ok')
