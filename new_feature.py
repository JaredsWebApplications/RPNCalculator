#!/usr/bin/env python3.8

import re
curly_brace_re_ = r"\{(.*?)\}"

# regular range notation
s = "1-10"
# bash expansion notation
st = "{1..10}"

# range of values

def range_(s: str) -> list:
  """
  We get a list of values from range n to k.
  This needs to be treated as it's own object, like a number and can be pushed to the stack.
  Operations can be applied to containers.
  """
  if(('-' in s and s[0] != '-')):
    split = s.split('-')
    range_tuple_ = (int(split[0]), int(split[1])+1)

  else:
    match = re.findall(curly_brace_re_, s)[0].split('..')
    range_tuple_ = (int(match[0]), int(match[1])+1)
  
  return [element for element in range(range_tuple_[0], range_tuple_[1])]

def percent(s: str) -> float:
    """
    Give the percent value of a number if in the format of <number>%.
    The number can either be an integer or float.
    """

    return float(s.split('%')[0])*0.01

def test_():
  test_list_ = [element for element in range(1, 11)]
  if(range_(s) == test_list_): print("passed regular range notation test")
  if(range_(st) == test_list_): print("passed bash expansion notation test")
  if(percent('5%') == 0.05): print("passed percent notation test")

test_()

# examples with percent
# ---- 1 ----------
# 5% =a
# will assign the variable with value of 0.05

# ----- 2 --------
# 10 5% *
# will return the value of 0.5


# examples with range
# ----- 1 -----
# {1..10} *
# get an float result of all elements in the list multiplied together
# e.g) 1 * 2 ...... * 10 = 3628800
