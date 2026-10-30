import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output

print(2026, 10, 18, sep="-")
print("Loading", end="...")
print("done!")

check_output("2026-10-18\nLoading...done!", hint="Try print(2026, 10, 18, sep=...) and print('Loading', end=...).")
