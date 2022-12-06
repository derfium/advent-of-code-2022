def task_1():
    with open("resources/inputFiles/input6.txt") as f:
        line = f.readline().replace("\n", "")
        
        for i, _ in enumerate(line, start=4):
            signal = line[i-4:i]
            
            if(checkSignal(signal)):
                return i
            
        return -1
    
def task_2():
    with open("resources/inputFiles/input6.txt") as f:
        line = f.readline().replace("\n", "")
        
        startOfPacket = task_1()
        
        for i, _ in enumerate(line, start=startOfPacket+14):
            signal = line[i-14:i]
            if checkSignal(signal):
                return i
    
    
def checkSignal(signal:str)->bool:
    for char in signal:
        if signal.count(char) != 1:
            return False
    return True
    
print(task_1())
print(task_2())