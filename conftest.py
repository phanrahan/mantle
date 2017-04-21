# content of conftest.py
import sys

collect_ignore = ["setup.py"]
if sys.version_info[0] < 3:
    collect_ignore.append("tests/mantle40/test_expressions/test_expressions.py")
