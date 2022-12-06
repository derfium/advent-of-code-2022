def task_1():
  with open("resources/inputFiles/input3.txt") as f:
    lines = f.readlines()
    prio = 0

    for line in lines:
      line = line.replace("\n", "")

      comp1 = sorted(line[:int(len(line)/2)])
      comp2 = sorted(line[int(len(line)/2):])
     
      for char in comp1:
        if comp2.__contains__(char):
          prio += getCharValue(char)
          break
      
    return prio


def task_2():
  with open("resources/inputFiles/input3.txt") as f:
    lines = f.readlines()
    prio = 0
    
    for i, _ in enumerate(lines):
      if i % 3 != 0: continue
      
      for char in lines[i]:
        if lines[i+1].__contains__(char) and lines[i+2].__contains__(char):
          prio += getCharValue(char)
          break
        
    return prio
      
      
def getCharValue(char:str):
  offset = 38 if char.isupper() else 96
  return ord(char) - offset
         
      
print(task_1())
print(task_2())