from pre import demand, csr#, # output
from check import *
from main import check_feasibility
from module3 import sum_of_month_lack

days = 31

output = {12: [-1, 0, 11, 0, 7, 7, 2, 0, 2, 11, 0, 7, 7, 0, 4, 3, 11, 3, 7, 7, 0, 2, 3, 11, 0, 7, 7, 3, 4, 0, 11, 2], 19: [-1, 0, 0, 0, 8, 8, 4, 11, 4, 4, 0, 8, 8, 2, 11, 2, 0, 2, 8, 8, 0, 11, 4, 0, 2, 8, 8, 0, 11, 1, 2, 1], 20: [-1, 7, 7, 1, 0, 2, 11, 0, 7, 7, 0, 3, 1, 11, 1, 7, 7, 0, 3, 0, 11, 3, 7, 7, 0, 3, 0, 11, 0, 7, 7, 1], 23: [-1, 8, 8, 3, 0, 11, 4, 4, 8, 8, 1, 0, 11, 3, 0, 8, 8, 2, 0, 11, 2, 0, 8, 8, 3, 0, 11, 0, 1, 8, 8, 0], 30: [-1, 0, 11, 7, 7, 0, 0, 1, 3, 11, 7, 7, 0, 2, 1, 0, 11, 7, 7, 1, 0, 3, 1, 11, 7, 7, 0, 0, 2, 1, 11, 7], 36: [-1, 12, 0, 8, 8, 1, 4, 0, 12, 0, 8, 8, 0, 1, 2, 12, 0, 8, 8, 4, 2, 0, 12, 1, 8, 8, 0, 2, 3, 12, 0, 8], 37: [-1, 9, 9, 0, 2, 11, 3, 0, 9, 9, 1, 0, 11, 0, 2, 9, 9, 0, 3, 11, 3, 0, 9, 9, 2, 0, 11, 0, 4, 9, 9, 1], 40: [-1, 0, 2, 12, 3, 1, 10, 10, 0, 0, 0, 12, 1, 10, 10, 0, 4, 4, 12, 0, 10, 10, 1, 0, 2, 12, 0, 10, 10, 2, 4, 4], 45: [-1, 11, 0, 9, 9, 2, 2, 0, 11, 1, 9, 9, 0, 3, 0, 11, 3, 9, 9, 2, 0, 2, 11, 0, 9, 9, 0, 2, 1, 11, 0, 9], 49: [-1, 8, 8, 0, 11, 4, 0, 1, 8, 8, 0, 11, 1, 0, 3, 8, 8, 3, 0, 0, 11, 1, 8, 8, 2, 1, 0, 4, 0, 11, 8, 8], 69: [-1, 12, 4, 0, 2, 0, 10, 10, 12, 0, 2, 1, 0, 10, 10, 12, 0, 1, 2, 0, 10, 10, 12, 0, 4, 3, 0, 10, 10, 12, 4, 1], 70: [-1, 10, 0, 10, 11, 0, 3, 3, 10, 0, 10, 0, 11, 4, 0, 10, 3, 10, 1, 11, 0, 2, 10, 3, 10, 0, 1, 13, 0, 10, 3, 10], 72: [-1, 12, 0, 0, 7, 8, 2, 1, 0, 3, 0, 7, 8, 2, 0, 12, 1, 0, 7, 8, 3, 0, 12, 4, 4, 7, 8, 1, 0, 12, 1, 4], 73: [-1, 9, 9, 0, 2, 12, 1, 2, 9, 9, 0, 0, 12, 2, 1, 0, 2, 9, 9, 12, 4, 0, 2, 0, 9, 9, 12, 0, 2, 1, 0, 9], 74: [-1, 12, 2, 8, 0, 8, 0, 1, 12, 1, 0, 3, 8, 8, 0, 12, 0, 1, 1, 8, 8, 0, 12, 2, 0, 2, 8, 8, 0, 12, 2, 2], 75: [-1, 10, 10, 2, 0, 1, 3, 11, 10, 10, 0, 2, 0, 2, 11, 10, 10, 3, 0, 2, 0, 11, 10, 10, 0, 4, 0, 3, 11, 10, 10, 0], 84: [-1, 0, 11, 0, 7, 7, 2, 0, 3, 11, 2, 2, 7, 7, 3, 0, 11, 3, 2, 7, 7, 2, 0, 11, 0, 3, 7, 7, 4, 0, 11, 0], 90: [-1, 3, 12, 9, 2, 0, 9, 0, 1, 12, 9, 0, 2, 9, 4, 2, 11, 0, 9, 1, 0, 9, 2, 11, 0, 0, 9, 4, 9, 0, 11, 3], 98: [-1, 3, 0, 11, 4, 10, 10, 0, 3, 2, 11, 0, 10, 10, 0, 4, 1, 6, 11, 0, 0, 10, 10, 4, 2, 11, 2, 0, 10, 10, 0, 2], 118: [-1, 4, 11, 0, 4, 0, 9, 9, 0, 11, 0, 3, 0, 9, 9, 0, 11, 4, 1, 0, 9, 9, 3, 3, 11, 3, 0, 9, 9, 4, 1, 11], 120: [-1, 7, 12, 7, 1, 2, 0, 3, 7, 12, 7, 3, 0, 4, 0, 7, 12, 7, 0, 4, 4, 4, 7, 12, 0, 7, 0, 3, 0, 7, 12, 0], 121: [-1, 1, 2, 11, 0, 3, 2, 8, 0, 2, 9, 11, 0, 2, 8, 3, 1, 0, 11, 0, 8, 8, 0, 1, 11, 4, 0, 8, 8, 0, 2, 11], 122: [-1, 3, 8, 8, 12, 0, 1, 0, 4, 8, 8, 0, 12, 4, 3, 3, 8, 8, 0, 1, 12, 1, 2, 0, 8, 0, 8, 0, 12, 2, 0, 8], 129: [-1, 0, 4, 11, 2, 7, 7, 0, 2, 3, 11, 2, 4, 0, 7, 7, 0, 11, 4, 0, 1, 7, 7, 2, 11, 0, 4, 0, 7, 7, 0, 11], 132: [-1, 2, 0, 12, 1, 0, 9, 9, 0, 1, 12, 4, 0, 9, 9, 2, 1, 12, 0, 0, 9, 9, 1, 2, 12, 3, 0, 4, 0, 9, 9, 12], 136: [-1, 8, 8, 0, 11, 3, 0, 1, 8, 0, 8, 11, 0, 2, 4, 0, 8, 8, 11, 1, 4, 0, 4, 8, 8, 11, 2, 0, 3, 4, 0, 8], 144: [-1, 2, 10, 2, 10, 11, 0, 2, 1, 0, 5, 10, 0, 11, 0, 10, 2, 2, 0, 10, 11, 2, 10, 4, 0, 4, 10, 0, 1, 11, 10, 0], 158: [-1, 9, 9, 12, 0, 3, 4, 0, 9, 9, 12, 0, 2, 3, 1, 9, 0, 12, 9, 0, 1, 3, 0, 9, 11, 0, 9, 2, 0, 4, 9, 11], 170: [-1, 2, 2, 2, 12, 0, 8, 8, 2, 2, 0, 12, 0, 8, 8, 1, 4, 0, 12, 2, 8, 8, 0, 0, 4, 12, 0, 8, 8, 0, 2, 4], 171: [-1, 3, 1, 2, 12, 8, 0, 8, 2, 0, 1, 12, 0, 8, 0, 8, 1, 2, 12, 0, 8, 4, 8, 3, 0, 12, 0, 8, 1, 8, 0, 1], 172: [-1, 11, 0, 9, 3, 9, 0, 2, 11, 0, 9, 2, 9, 0, 2, 11, 0, 9, 0, 9, 1, 2, 0, 11, 9, 2, 9, 2, 2, 0, 11, 9], 186: [-1, 0, 2, 10, 10, 11, 2, 0, 1, 3, 0, 10, 11, 0, 10, 2, 0, 4, 10, 11, 0, 2, 10, 1, 4, 0, 11, 10, 3, 2, 10, 0], 190: [-1, 10, 0, 10, 4, 12, 1, 3, 0, 10, 10, 0, 4, 11, 0, 3, 0, 10, 0, 10, 11, 1, 1, 0, 10, 1, 0, 11, 1, 10, 2, 10], 203: [-1, 1, 2, 0, 1, 9, 11, 9, 4, 0, 3, 0, 9, 12, 9, 0, 2, 3, 0, 9, 12, 9, 0, 2, 0, 2, 0, 12, 9, 9, 4, 2], 208: [-1, 1, 3, 1, 0, 10, 12, 10, 1, 1, 0, 0, 10, 12, 10, 2, 0, 3, 0, 10, 12, 10, 0, 4, 0, 3, 0, 12, 10, 10, 4, 2], 213: [-1, 11, 1, 9, 9, 0, 3, 2, 11, 0, 9, 9, 0, 3, 0, 11, 1, 9, 9, 0, 4, 2, 11, 0, 9, 9, 0, 2, 0, 11, 2, 9], 231: [-1, 1, 11, 10, 10, 0, 2, 0, 1, 11, 10, 10, 0, 4, 0, 1, 11, 10, 0, 0, 10, 4, 4, 11, 10, 0, 1, 10, 4, 0, 11, 10], 239: [-1, 2, 0, 12, 2, 0, 7, 7, 0, 1, 12, 2, 4, 7, 7, 0, 3, 12, 0, 2, 7, 7, 0, 2, 12, 0, 4, 7, 7, 0, 2, 12], 241: [-1, 4, 2, 0, 12, 4, 0, 9, 9, 4, 0, 12, 0, 0, 9, 9, 4, 4, 12, 0, 1, 9, 9, 4, 2, 12, 0, 4, 9, 9, 0, 2], 249: [-1, 1, 1, 1, 10, 0, 10, 11, 1, 0, 2, 0, 10, 10, 11, 0, 4, 0, 3, 0, 10, 11, 10, 0, 4, 3, 2, 10, 11, 0, 10, 2]}

check_legal_leaves(output, days)
check_consecutive_workdays(output, days)
check_night_shift(output, days)
check_afternoon_shift(output, days)
check_feasibility(output)
print(sum_of_month_lack(output, days, demand))