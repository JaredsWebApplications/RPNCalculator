#!/usr/bin/env python

from enum import IntEnum


class operand_codes(IntEnum):
    SIN = 0
    COS = 1
    TAN = 2
    EXP = 3
    POW = 4
    ADD = 5
    SUB = 6
    MUL = 7
    DIV = 8
    MOD = 9
    ASIN = 10
    ACOS = 11
    ATAN = 12
    SINH = 13
    COSH = 14
    TANH = 15
    ASINH = 16
    ACOSH = 17
    ATANH = 18
    LOG = 19
    LN = 20
    FLOOR = 21
    SQRT = 22
    GARBAGE = 23
    LINEFEED = 24
    NUMBER = 25
    ASSIGN = 26
    RETRIEVE = 27
    POP = 28
    PEEK = 29
    CONSTANT = 30
    COMMENT = 31


# G = graviational constant
# g = gravity on Earth


class constants(IntEnum):
    _PI = 0
    _G = 1
    _g = 2
    _e = 3


class lexer:
    def __init__(self):
        self.operands_names_ = [operand.name for operand in operand_codes]
        self.constant_names_ = [constant.name for constant in constants]
        self.keywords = self.operands_names_ + self.constant_names_
        self.operand_map = {
            "+": operand_codes.ADD.value,
            "-": operand_codes.SUB.value,
            "/": operand_codes.DIV.value,
            "%": operand_codes.MOD.value,
            "*": operand_codes.MUL.value,
            "\n": operand_codes.LINEFEED.value,
        }

    def is_keyword(self, pattern: str) -> bool:
        """
        Check if given token given is a keyword.
        If it is, then we cannot use it for variable assignment.
        """
        return pattern in self.keywords

    def is_number(self, element: str) -> bool:
        integer_check_ = element.isdigit()
        try:
            float(element)
            float_check_ = True
        except ValueError:
            float_check_ = False
        return integer_check_ or float_check_

    def tokenize(self, token: str) -> int:
        """
        Iterate over the token names.
        If there is a match, return it's operand code.
        If there is not a match, return a garbage value.
        """
        if token in self.operands_names_:
            return getattr(operand_codes, token).value
        if self.is_number(token):
            return operand_codes.NUMBER.value
        if token[0] == "=":
            return operand_codes.ASSIGN.value
        if token[0] == "?":
            return operand_codes.RETRIEVE.value
        if token[0] == "_":
            return operand_codes.CONSTANT.value
        if token[0] == "#":
            return operand_codes.COMMENT.value
        try:
            return self.operand_map[token]
        except KeyError:
            return operand_codes.GARBAGE.value
