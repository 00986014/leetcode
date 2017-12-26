def evalRPN(tokens):
    stack = []
    for s in tokens:
        if s == '+':
            a = int(stack[-2])+int(stack[-1])
            stack.pop()
            stack.pop()
            stack.append(str(a))
            print stack
        elif s == '-':
            a = int(stack[-2])-int(stack[-1])
            stack.pop()
            stack.pop()
            stack.append(str(a))
            print stack
        elif s == '*':
            a = int(stack[-2])*int(stack[-1])
            stack.pop()
            stack.pop()
            stack.append(str(a))
            print stack
        elif s == '/':
            if int(stack[-2])<0 and int(stack[-1])>0:
                a = -(abs(int(stack[-2]))/int(stack[-1]))
            elif int(stack[-2])>0 and int(stack[-1])<0:
                a = -((int(stack[-2]))/abs(int(stack[-1])))
            else:
                a = int(stack[-2])/int(stack[-1])
            stack.pop()
            stack.pop()
            stack.append(str(a))
            print stack
        else:
            stack.append(s)
            print stack
    return int(stack[0])
