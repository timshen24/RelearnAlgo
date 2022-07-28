# Given a list containing lines with the format "time,value" corresponding
# to a series of values along time, and an integer windowSize, I want to compute
# a moving average of the values in a window of size windowSize. For example for
# the input
# ```
# 1,20
# 2,80
# 3,40
# 4,60
# ```
# and windowSize equal to 2 then the output should be
# ```
# 1, 10.0
# 2, 50.0
# 3, 60.0
# 4, 50.0
# 5, 30.0
# ```
# Assume a value of 0 for missing elements (e.g. elements before the first one,
# or after the last one)
#
# No window function allowed
