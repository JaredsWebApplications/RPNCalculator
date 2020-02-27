#!/usr/bin/env python3.8

import math
from stack import stack
from lexer import lexer, operand_codes
import maths

stack_ = stack()
lex = lexer()

example = "3 2 POW"
example_ = example.split()

variable_map_ = {
    "variable": 10.0
}

for chunk in example_:
  operand_code = lex.tokenize(chunk)
  if(operand_code == operand_codes.GARBAGE.value):
    print("got garbage with operand: {}".format(chunk))
  elif(operand_code == operand_codes.NUMBER.value):
    print("pushing value of: {}".format(chunk))
    stack_.push(float(chunk))
  elif(operand_code == operand_codes.ASSIGN.value):
    if(lex.is_keyword(chunk)):
      print("cannot use {} as a variable name!".format(chunk))
      stack_.clear_contents()
      break
    else:
      print("assigning {} with value of {}".format(chunk[1:], stack_.peek()))
      variable_ = chunk[1:]
      value_ = stack_.peek()
      variable_map_[variable_] = value_
  elif(operand_code == operand_codes.RETRIEVE.value):
    variable_ = chunk[1:]
    try:
        value_retrieved_ = variable_map_[variable_]
        print("retrieved varaible {} with value of {}".format(variable_, value_retrieved_))
    except KeyError:
        print("cannot retrieve value of {}, it is not in the table".format(variable_))
  else:
    # implement this into long math function
    # math_function(container: list, operand_code: int)
# if len at least 1 or ge than two then the add, sub, etc operands
    try:
      multi_argument_code = lex.operand_map[chunk]
      contents_ = stack_.data_.copy()
      stack_.clear_contents()
      stack_.push(maths.math_function(contents_, multi_argument_code))
    except KeyError:
      value_ = [stack_.pop()]
      if(operand_codes.POW.value == lex.tokenize(chunk)):
        value_.append(stack_.pop())
      stack_.clear_contents()
      try:
        stack_.push(float(maths.math_function(value_, lex.tokenize(chunk))))
      except Exception as error:
        print("oops, got a math error ey there bud!: {}".format(error))

print(stack_.peek())
