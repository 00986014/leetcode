def isValid(s):
    stack = []
    for i in s:
        if i =='(' or i == '[' or i == '{':
            stack.append(i)
        else:
            if not stack: 
                return False
            if stack[-1] == '(' and i == ')':
                stack.pop()
            elif stack[-1] == '[' and i == ']':
                stack.pop()
            elif stack[-1] == '{' and i == '}':
                stack.pop()
            else:
                return False
    return stack==[]
