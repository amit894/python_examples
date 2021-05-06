open_bracket=["{","[","("]
close_bracket=["}","]",")"]

def valid_pranthesis(string):
    s1=[]
    for ch in string:
        if ch in open_bracket:
            s1.append(ch)
        elif ch in close_bracket:
            pos=close_bracket.index(ch)
            if open_bracket[pos] in s1:
                s1.pop()
    if (len(s1))==0:
        return True
    else:
        return False


print(valid_pranthesis("()"))
print(valid_pranthesis("()[]{}"))
print(valid_pranthesis("(]"))
print(valid_pranthesis("([)]"))
print(valid_pranthesis("{[]}"))
