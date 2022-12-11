from math import floor


class Monkey(object):
    itemList: list = []
    operation: any = None
    testDiv: int = 0
    trueTest: int = 0
    falseTest: int = 0
    inspectionCounter: int = 0
    
    def __init__(self, itemList, operation,  testDiv, trueTest, falseTest):
        self.itemList = itemList
        self.operation = operation
        self.testDiv = testDiv
        self.trueTest = trueTest
        self.falseTest = falseTest
    

def task_1():
    with open("resources/inputFiles/input11.txt") as f:
        lines = f.read().splitlines()
        monkeys = parseMonkeys(lines)
        
        for _ in range(20):
            monkeys = performRound(monkeys)
        monkeys.sort(key=lambda monkey: monkey.inspectionCounter, reverse=True)
        return monkeys[0].inspectionCounter * monkeys[1].inspectionCounter
                        
            
def performRound(monkeys:list[Monkey]):
    for monkey in monkeys:
        while monkey.itemList:
            item = monkey.itemList.pop(0)
            newWorryLevel = monkey.operation(item)
            newWorryLevel = floor(newWorryLevel / 3)
            monkey.inspectionCounter += 1
            if newWorryLevel % monkey.testDiv == 0:
                assert(monkey.trueTest <= len(monkeys))
                monkeys[monkey.trueTest].itemList.append(newWorryLevel)
            else:
                assert(monkey.falseTest <= len(monkeys))
                monkeys[monkey.falseTest].itemList.append(newWorryLevel)

    return monkeys                
                
            
def parseMonkeys(lines: list):   
    monkeys = []
    for i, line in enumerate(lines):
        if line.startswith("Monkey"):
            startingItems = list(map(int, lines[i + 1].split(": ")[1].split(",")))
            operation = parseOperation(lines[i + 2])
            modulo = int(lines[i + 3].replace("Test: divisible by ", ""))
            trueTest = int(lines[i + 4].split(" ")[9])
            falseTest = int(lines[i + 5].split(" ")[9])
            monkey = Monkey(startingItems, operation, modulo, trueTest, falseTest)
            monkeys.append(monkey)
    return monkeys
            
        
def parseOperation(line: str):
    line = line.replace("Operation: new = old ", "")
    values = list(filter(lambda x: len(x) != 0, line.split(" ")))
    match values[0]:
        case "+": return lambda x: x + int(values[1])
        case "*":
            if (values[1] == "old"):
                return lambda x: x**2
            return lambda x: x * int(values[1])

        
                
print("Task 1 =", task_1())
            
            
        
        