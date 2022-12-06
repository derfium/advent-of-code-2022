def task_1(reverse):
    with open("src/input5.txt") as f:
        lines = f.readlines()
        
        stack = fillStacks(lines)
        
        for line in lines:
            if not line.startswith("m"): continue
            line = line.replace("\n", "")
            
            ints = line.split(" ")
            rInts = []
            for i in ints:
                try: 
                    i = int(i)
                    rInts.append(i)
                except: continue
            amount = rInts[0]
            fromInt = rInts[1]-1
            toInt = rInts[2]-1
            stack = movement(stack, amount, fromInt, toInt, reverse)
        return getResult(stack)
            
                    
def movement(stack, amount, fromInt, toInt, reverse):
    tmpStack = []
    for i in range(amount):
        tmp = stack[fromInt].pop()
        tmpStack.append(tmp)
    if reverse: tmpStack.reverse()
    for elem in tmpStack:
        stack[toInt].append(elem)
    return stack

def fillStacks(lines):
    stack = []
    stackLines = []
    for line in lines:
        line = str(line).replace("\n", "")

        if line.__contains__("["):
            stackLines.append(line)
            continue

        line = line.replace(" ", "")
        
        
        for _ in range(len(line)):
            stack.append([])
        break
    
    
    stackLines.reverse()
    for line in stackLines:
        spaceCounter = 0
        
        line = str(line).replace("\n", "")
        elements = line.split(" ")
        
        for element in elements:
            if element == "":
                spaceCounter += 1
            else:
                stackRank = int(spaceCounter / 4)
                stack[stackRank].append(element.replace("[", "").replace("]", ""))
                spaceCounter += 4
    return stack
  
def getResult(stack):
    ret = ""
    for s in stack:
        top = s[len(s)-1::][0]
        ret = ret.__add__(top)
    return ret

def getMovementInput(lines):
    ret = []
    for line in lines:
        if str(line).startswith("w"):
            ret.append(line)
    return ret

def getSetupInput(lines):
    ret = []
    for line in lines:
        if line: pass
        

def task_2():
    with open("src/input5.txt") as f:
        pass


print("t1 =", task_1(False))
print("t2 =", task_1(True))