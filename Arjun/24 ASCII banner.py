print("+--------------+")
print("|  Welcome to  |")
print("|    Python    |")
print("+--------------+")

import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output

check_output("+--------------+\n|  Welcome to  |\n|    Python    |\n+--------------+")
