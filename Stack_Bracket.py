def checkIntegrity(expression):
    stack = []
    #Define a list of opening brackets
    ob =['(', '{', '[']
    
    
    #When you encounter a opening parenthesis, push it to the stack
    for bracket in expression:
        if bracket in ob:
            stack.append(bracket)
            
        else:
            if not stack:
                return "Not Ok"
            current_character = stack.pop()
            #For the closed bracket popped, check the opening brackets
            if current_character == ")":
                if bracket == "(":
                    return "Ok"
            if current_character == "}":
                if bracket == "{":
                    return "Ok"
            if current_character == "]":
                if bracket == "[":
                    return "Ok"
    #if the stack is not empty
    if stack:
        return "Not Ok"
   
    return "OK"
    
## Test print to check the integrity of brackets

expression1 = "{[[]]{()}"
checkIntegrity(expression1)

expression2 = "[{}]"
checkIntegrity(expression2)
