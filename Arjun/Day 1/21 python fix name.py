print("Hello, Python 3")

import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output

check_output("Hello, Python 3")
