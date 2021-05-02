open_list = ["[","{","("]
close_list = ["]","}",")"]

def is_balanced(str):
    stack=[]
    for ch in str:
        if ch in open_list:
            stack.append(ch)
        elif ch in close_list:
            pos=close_list.index(ch)
            if (len(stack)>0) and (open_list[pos]==stack[len(stack)-1]):
                stack.pop()
    if len(stack)==0:
        return "balanced" 
    else:
        return "unbalanced"

string = " {[()]}"
print(string,"-", is_balanced(string))

string = "{[(])}"
print(string,"-", is_balanced(string))

string = "{{[[(())]]}}"
print(string,"-",is_balanced(string))
