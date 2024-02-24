#! /bin/env python

import re
import shutil
from pathlib import Path


for file in Path('./source/posts/').rglob("*.rst"):
    file_content = file.read_text(encoding='latin-1')
    file_img_dir = file.stem.rsplit('-', maxsplit=1)[-1]
    file_img_dirpath = Path(f'./source/_static/img/posts/{file_img_dir}')
    file_img_dirpath.mkdir(exist_ok=True)
    for match in re.findall(r".. image:: (.*)", file_content):
        old_file_img_path = Path(match.replace('..', './source/posts/'))
        if not old_file_img_path.exists():
            continue
        new_file_img_path = file_img_dirpath / old_file_img_path.name
        shutil.move(old_file_img_path, new_file_img_path)
        new_file_ref = match.replace('../imgs', f'../_static/img/posts/{file_img_dir}')
        file_content = re.sub(match, new_file_ref, file_content)
    file.write_text(file_content, encoding='latin-1')
