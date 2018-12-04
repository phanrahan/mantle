import os
import shutil

for filename in os.listdir('tests/test_greenpak4/gold'):
    try:
        shutil.copy(os.path.join("tests/test_greenpak4/build", filename),
                    os.path.join("tests/test_greenpak4/gold", filename))
    except FileNotFoundError:
        os.system(f"git rm {os.path.join('tests/test_greenpak4/gold', filename)}")
