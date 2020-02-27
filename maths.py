#!/usr/bin/env python3.8

from lexer import operand_codes
import math
import stack
import functools
import operator

function_map_ = {
    operand_codes.SIN.value: lambda a : math.sin(a),
    operand_codes.COS.value: lambda a: math.cos(a),
    operand_codes.TAN.value: lambda a: math.tan(a),
    operand_codes.ASIN.value: lambda a: math.asin(a),
    operand_codes.ACOS.value: lambda a: math.acos(a),
    operand_codes.ATAN.value: lambda a: math.atan(a),
    operand_codes.SINH.value: lambda a: math.sinh(a),
    operand_codes.COSH.value: lambda a: math.cosh(a),
    operand_codes.TANH.value: lambda a: math.tanh(a),
    operand_codes.EXP.value: lambda a: math.exp(a),
    operand_codes.LOG.value: lambda a: math.log10(a),
    operand_codes.LN.value: lambda a: math.log(a),
    operand_codes.POW.value: lambda a, b: math.pow(a, b)
}
def math_function(container: list, operand_code: int) -> float:
    if(len(container) == 1):
      try:
          return function_map_[operand_code](*container)
      except KeyError:
          print("unsupported operand code: {}".format(operand_code))
    elif(len(container) == 2):
      try:
          return function_map_[operand_code](container[1], container[0])
      except KeyError:
          print("unsupported operand code: {}".format(operand_code))
    elif(len(container) >= 2):
      if(operand_code == operand_codes.ADD.value):
        return functools.reduce(operator.add, container)
      elif(operand_code == operand_codes.SUB.value):
        return functools.reduce(operator.sub, container)
      elif(operand_code == operand_codes.MUL.value):
        return functools.reduce(operator.mul, container)
      elif(operand_code == operand_codes.DIV.value):
        return functools.reduce(operator.truediv, container)
      elif(operand_code == operand_codes.MOD.value):
        return functools.reduce(operator.mod, container)
