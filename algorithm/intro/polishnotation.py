__author__ = 'congliu'
import math

def evalRPN(tokens):
        stack = []
        for token in tokens:
            if token not in '+-*/':
                stack.append(token)
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(str(int(eval(op1+token+op2))))
        return eval(stack[0])

tokens = ['4','13','5','/','+']
#tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

print(evalRPN(tokens))
