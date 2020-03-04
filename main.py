#!/usr/bin/env python3.8

import math
from stack import stack
from lexer import lexer, operand_codes
import maths
from signal import signal, SIGINT
from sys import exit

stack_ = stack()
lex = lexer()

example = "3 2 POW"

variable_map_ = {
    "variable": 10.0
}

def sigint_handler(signal_received, frame):
    exit(0)

def rpn_calculator(expression: str) -> None:
  for chunk in expression.split():
    operand_code = lex.tokenize(chunk)
    if(operand_code == operand_codes.GARBAGE.value):
      print("got garbage with operand: {}".format(chunk))

    elif(operand_code == operand_codes.NUMBER.value):
      stack_.push(float(chunk))

    elif(operand_code == operand_codes.ASSIGN.value):
      variable_ = chunk[1:]
      if(variable_.strip() in lex.keywords):
        print("cannot use {} as a variable name!".format(variable_))
        stack_.clear_contents()
        break
      else:
        print("assigning {} with value of {}".format(chunk[1:], stack_.peek()))
        variable_map_[variable_] = stack_.peek()

    elif(operand_code == operand_codes.RETRIEVE.value):
      variable_ = chunk[1:]
      try:
          value_retrieved_ = variable_map_[variable_]
          # print("retrieved varaible {} with value of {}".format(variable_, value_retrieved_))
          stack_.push(value_retrieved_)
      except KeyError:
          print("cannot retrieve value of {}, it is not in the table".format(variable_))
    else:
      try:
        # this is only for list operations
        multi_argument_code = lex.operand_map[chunk]
        contents_ = stack_.pop_n(2)
        try:
          stack_.push(maths.math_function(contents_, multi_argument_code))
        except TypeError as error:
          print("error value of: {}".format(error))
          print("invalid syntax: {}".format(chunk))
      except KeyError:
        value_ = [stack_.pop()]
        if(operand_codes.POW.value == lex.tokenize(chunk)):
          value_.append(stack_.pop())
        stack_.clear_contents()
        try:
          stack_.push(float(maths.math_function(value_, lex.tokenize(chunk))))
        except Exception as error:
          print("oops, got a math error ey there bud!: {}".format(error))

signal(SIGINT, sigint_handler)

while(True):
  exp = input(">>> ")
  rpn_calculator(exp)
  if(not stack_.is_empty()):
    try: print("\t{}".format(stack_.peek()))
    except IndexError: pass
  stack_.clear_contents()
