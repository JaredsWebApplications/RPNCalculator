#!/usr/bin/env python3.8

from lexer import operand_codes, lexer, constants
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
    operand_codes.FLOOR.value: lambda a: math.floor(a),
    operand_codes.SQRT.value: lambda a: math.sqrt(a),
    operand_codes.POW.value: lambda a, b: math.pow(a, b),
    operand_codes.ADD.value: lambda a, b: a + b,
    operand_codes.SUB.value: lambda a, b: a - b,
    operand_codes.MUL.value: lambda a, b: a * b,
    operand_codes.DIV.value: lambda a, b: a / b,
    operand_codes.MOD.value: lambda a, b: a % b
# operand_codes.LIST_ADD.value: lambda container: functools.reduce(operator.add, container)
    # operand_codes.ADD.value: lambda container: functools.reduce(operator.add, container),
    # operand_codes.SUB.value: lambda container: functools.reduce(operator.sub, container),
    # operand_codes.MUL.value: lambda container: functools.reduce(operator.mul, container),
    # operand_codes.DIV.value: lambda container: functools.reduce(operator.truediv, container),
    # operand_codes.MOD.value: lambda container: functools.reduce(operator.mod, container)
}

constant_map_ = {
  constants._PI.value: math.pi,
  constants._G.value: 6.67430E-11,
  constants._g.vaule: 9.81,
  constants._e.value: math.e
}

lexi = lexer()
simple_operands_ = list(lexi.operand_map.values())

def math_function(container: list, operand_code: int) -> float:
    if(container is None): return

    # if it is any of the trig functions
    try:
      if(len(container) == 1):
        return function_map_[operand_code](*container)
      elif(len(container) == 2 or operand_code == operand_codes.POW.value and operand_code in simple_operands_):
        return function_map_[operand_code](container[1], container[0])
      else:
        return function_map_[operand_code](container)
    except KeyError:
        print("unsupported operand code: {}".format(operand_code))
