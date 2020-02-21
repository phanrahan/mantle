"""
Expected to be run from repo root
"""
import shutil
import os


def copy_golds(dir_path):
    if not os.path.isdir(dir_path):
        return
    if "gold" in os.listdir(dir_path):
        for f in os.listdir(os.path.join(dir_path, "gold")):
            try:
                shutil.copy(
                    os.path.join(dir_path, "build", f),
                    os.path.join(dir_path, "gold", f),
                )
            except FileNotFoundError:
                os.remove(os.path.join(dir_path, "gold", f))

    for name in os.listdir(dir_path):
        copy_golds(os.path.join(dir_path, name))


for name in os.listdir("tests"):
    copy_golds(os.path.join("tests", name))
