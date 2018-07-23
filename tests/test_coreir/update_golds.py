import os
import shutil

for filename in os.listdir('gold'):
    try:
        shutil.copy(os.path.join("build", filename),
                    os.path.join("gold", filename))
    except FileNotFoundError:
        os.system(f"git rm {os.path.join('gold', filename)}")
