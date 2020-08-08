#! python3
#sysargtest.py
#just a test for system arguments orders.

import sys
v = {}
v[0] = sys.argv[0]
v[1] = sys.argv[1]
v[2] = sys.argv[2]
v[3] = sys.argv[3]
v[4] = sys.argv[4]
v[5] = sys.argv[5]
for i in range(6):
 	print(v[i])
print(sys.argv[0])