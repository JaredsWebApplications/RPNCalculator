#!/usr/bin/env python3.8

from aenum import Enum

class operand_codes(Enum, start=0):
    SIN
    COS
    TAN
    EXP
    POW
    ADD
    SUB
    MUL
    DIV
    MOD
    ASIN
    ACOS
    ATAN
    SINH
    COSH
    TANH
    ASINH
    ACOSH
    ATANH
    LOG
    LN
    GARBAGE
    LINEFEED
    NUMBER
    ASSIGN
    RETRIEVE
    POP
    PEEK


# G = graviational constant
# g = gravity on Earth
# PLANCK = Planck's constant

class constants(Enum, start=0):
    _PI
    _G
    _g
    _PLANCK
    _e


class lexer():
    def __init__(self):
        self.operands_names_ = [operand.name for operand in operand_codes]
        self.constant_names_ = [constant.name for constant in constants]
        self.keywords = self.operands_names_ + self.constant_names_
        self.operand_map = {
            '+': operand_codes.ADD.value,
            '-': operand_codes.SUB.value,
            '/': operand_codes.DIV.value,
            '%': operand_codes.MOD.value,
            '*': operand_codes.MUL.value,
            '\n': operand_codes.LINEFEED.value
        }

    def is_keyword(self, pattern: str) -> bool:
        """
        Check if given chunk given is a keyword.
        If it is, then we cannot use it for variable assignment.
        """
        return pattern in self.keywords

    def tokenize(self, chunk: str) -> int:
        """
        Iterate over the token names.
        If there is a match, return it's operand code.
        If there is not a match, return a garbage value.
        """
        if(chunk in self.operands_names_):
          return getattr(operand_codes, chunk).value
        if(chunk.isdigit()):
          return operand_codes.NUMBER.value
        if(chunk[0] == '='):
          return operand_codes.ASSIGN.value
        if(chunk[0] == '?'):
          return operand_codes.RETRIEVE.value
        try:
            return self.operand_map[chunk]
        except KeyError:
            return operand_codes.GARBAGE.value


