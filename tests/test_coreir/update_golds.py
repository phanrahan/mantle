import os
import shutil

for filename in os.listdir('tests/test_coreir/gold'):
    try:
        shutil.copy(os.path.join("tests/test_coreir/build", filename),
                    os.path.join("tests/test_coreir/gold", filename))
    except FileNotFoundError:
        os.system(f"git rm {os.path.join('tests/test_coreir/gold', filename)}")
