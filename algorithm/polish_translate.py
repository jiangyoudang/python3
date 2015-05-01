priority = {
    '(':0,
    '+':1, '-':1,
    '*':2, '/':2,
    ')':3
}

digits = '1234567890'
operators = '+-*/()'

d_stack = []
op_stack = []

def tranlate(s):
    for c in s:
        if c in digits:
            d_stack.append(c)
        elif c in operators:
            if c == '(':
                op_stack.append(c)
            elif c == ')':

                while op_stack[-1] != '(':
                    d_stack.append(op_stack.pop())
                op_stack.pop()

            else:
                while op_stack and priority[c] <= priority[op_stack[-1]]:
                    d_stack.append(op_stack.pop())

                op_stack.append(c)

        else:
            print('Invalid expression')
            break

    while op_stack:
        d_stack.append(op_stack.pop())
    return d_stack

test = '2*(1+2)/3*4-5'
print(tranlate(test))