# full_ops.py
#
# Usage: python3 full_ops.py c_in n_wv 
# Determine the output shape and operation count of an average pooling layer.
# Parameters:
# c_in: input channel count
# n_wv: number of weight vectors
# Output:
#  output channel count, output height count, output width count, number of additions, multiplications and divisions performed
#
# Written by Tejas Vinod
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.
#
# Test Inputs:
# python3 full_ops.py
# Expected Answer
# 


# import Python modules
import math # math module
import sys # argv

# "constants"
# none

# helper functions
# none

# initialize script arguments
c_in = float('nan') # input channel count
n_wv= float('nan') # number of weight vectors

# parse script arguments
if len(sys.argv)==3:
    c_in = float(sys.argv[1]) # input channel count
    n_wv = float(sys.argv[2]) # number of weight vectors
else:
  print(\
   'Usage: '\
   'python3 full_ops.py c_in n_wv'\
  )
  exit()

# write script below this lin
c_out = n_wv
h_out = 1
w_out = 1
adds = n_wv*c_in
muls = n_wv*c_in
divs = 0 

print(int(c_out)) # output channel count
print(int(h_out)) # output height count
print(int(w_out)) # output width count
print(int(adds))  # number of additions performed
print(int(muls))  # number of multiplications performed
print(int(divs))  # number of divisions performed