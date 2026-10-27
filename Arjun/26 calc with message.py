import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output

print("Area of a 12 by 7 room:", 12*7, "square metres")

check_output("Area of a 12 by 7 room: 84 square metres", hint="print('Area of a 12 by 7 room:', 12 * 7, 'square metres')")
