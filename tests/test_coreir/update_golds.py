import os
import shutil
for filename in os.listdir('gold'):
    shutil.copy(os.path.join("build", filename), os.path.join("gold", filename))
