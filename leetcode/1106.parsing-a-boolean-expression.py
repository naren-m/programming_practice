#
# @lc app=leetcode id=1106 lang=python3
#
# [1106] Parsing A Boolean Expression
#
# https://leetcode.com/problems/parsing-a-boolean-expression/description/
#
# algorithms
# Hard (59.57%)
# Total Accepted:    3.3K
# Total Submissions: 5.6K
# Testcase Example:  '"!(f)"'
#
# Return the result of evaluating a given boolean expression, represented as a
# string.
# 
# An expression can either be:
# 
# 
# "t", evaluating to True;
# "f", evaluating to False;
# "!(expr)", evaluating to the logical NOT of the inner expression expr;
# "&(expr1,expr2,...)", evaluating to the logical AND of 2 or more inner
# expressions expr1, expr2, ...;
# "|(expr1,expr2,...)", evaluating to the logical OR of 2 or more inner
# expressions expr1, expr2, ...
# 
# 
# 
# Example 1:
# 
# 
# Input: expression = "!(f)"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: expression = "|(f,t)"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: expression = "&(t,f)"
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: expression = "|(&(t,f,t),!(t))"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= expression.length <= 20000
# expression[i] consists of characters in {'(', ')', '&', '|', '!', 't', 'f',
# ','}.
# expression is a valid expression representing a boolean, as given in the
# description.
# 
#
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def convertToBool(e):
            if e == 'f':
                return False
            elif e == 't':
                return True
            else:
                raise Exception
        
        def convertBoolToStr(e):
            if e is True:
                return 't'
            elif e is False:
                return 'f'
            else:
                raise Exception

        def applyOperator(operator, operands):
            if operator == '&':
                return all(operands)
            elif operator == '|':
                return any(operands)
            elif operator == '!' and len(operands) == 1:
                return not operands[0]
            else:
                raise Exception

        def isOperator(o):
            if o in ['&', '|', '!']:
                return True
            else:
                return False

        def isOperand(o):
            if o in ['t', 'f']:
                return True
            else:
                return False



        stack = list()
        for e in expression:
            if e == ',':
                continue
            # print(stack, e)
            if isOperator(e):
                stack.append(e)
            elif e == '(':
                stack.append('(')
            elif isOperand(e):
                stack.append(convertToBool(e))
            elif e == ')':
                operands = list()
                while len(stack) > 0:
                    _e = stack.pop()
                    if _e == '(':
                        _o = stack.pop()
                        result = applyOperator(_o, operands)
                        # print('Popping', stack, e, _o)
                        stack.append(result)
                        break
                        # print(result)
                    operands.append(_e)
        
        return result

		
# s = Solution()
# expr = "|(f,t)"
# print(s.parseBoolExpr(expr))
