#!/usr/bin/env python3.8
import functools
import operator

nums = [1.232, 1.342]

print(functools.reduce(operator.sub, nums))
