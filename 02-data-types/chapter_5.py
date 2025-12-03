# Real Numbers and Float in Python -> Real number means precision in programming.
import sys
from fractions import Fraction
from decimal import Decimal, getcontext # we will uss D to represent the decimal values.
getcontext().prec = 22
# Decimal(1)/Decimal(3)
print(f"Decimal value of 1/3: {Decimal(1)/Decimal(3)}")

ideal_temp = 90.23
current_temp = 93.24234143280813413

print(f"Ideal temp: {ideal_temp}")
print(f"Current temp: {current_temp}")
print(f"Different temp: {ideal_temp - current_temp}")
print(sys.getsizeof(current_temp))
# print(sys.float_info) 
#sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1) this give us the float point information of the system it can be vary system to system.