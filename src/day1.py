def task_1():
  with open("resources/input1.txt") as f:
    lines = f.readlines()
    max = 0
    currentAcc = 0
    
    for line in lines:
      line = line.replace('\n', '')
      if (line == ''):
        if (currentAcc > max):
          max = currentAcc
        currentAcc = 0
      else:
        value = int(line)
        currentAcc += value

    return max
   
 
def task_2():
  with open("resources/input1.txt") as f:
    a_lines = f.readlines()
    a_max = [0, 0, 0]
    currentAcc = 0
    
    for line in a_lines:
      line = line.replace('\n', '')
      
      if (line == ''):
        smallestIndex = a_max.index(min(a_max))
        if currentAcc >= a_max[smallestIndex]:
          a_max[smallestIndex] = currentAcc
        currentAcc = 0
      else:
        value = int(line)
        currentAcc += value
        
    return sum(a_max)
