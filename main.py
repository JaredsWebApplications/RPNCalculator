#!/usr/bin/env python3.8

import math
from stack import stack
from lexer import lexer, operand_codes

stack_ = stack()
lex = lexer()

example = "?variable"
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
    print("got something: {}".format(chunk))
