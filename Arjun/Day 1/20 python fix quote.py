print("Python is Great")

import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output

check_output("Python is Great")
