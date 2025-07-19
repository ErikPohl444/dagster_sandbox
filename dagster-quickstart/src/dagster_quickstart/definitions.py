from pathlib import Path

from dagster import definitions, load_from_defs_folder


@definitions
def defs():
    print(Path(__file__).parent.parent.parent)
    return load_from_defs_folder(project_root=Path(__file__).parent.parent.parent)
