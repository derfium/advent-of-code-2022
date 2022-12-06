def task_1():
  with open("src/input2.txt") as f:
    a = f.readlines()
    
    overallPoints = 0
    
    for line in a:
      
      line = line.replace("\n", "")
      if line == "":
        continue
      otherSelection = line.split(" ")[0]
      mySelection = line.split(" ")[1]
      
      winPoints = play(otherSelection, mySelection)
      selectionPoints = getSelectionPoints(mySelection)
      
      overallPoints += (winPoints + selectionPoints)
      
    return overallPoints
      
      

def task_2():
  with open("src/input2.txt") as f:
    lines = f.readlines()
    overallPoints = 0
    
    for line in lines:
      line.replace("\n", "")
      
      otherSelection = line.split(" ")[0].replace(" ", "")
      outcome = line.split(" ")[1].replace("\n", "")
      mySelection = calculateSelection(otherSelection, outcome)

      winPoints = play(otherSelection, mySelection)
      selectionPoints = getSelectionPoints(mySelection)
            
      overallPoints += (winPoints + selectionPoints)
      
    return overallPoints
      
      

def calculateSelection(enemySelection:str, outcome:str):
  # X=LOSE, Y=DRAW, Z=WIN
  match enemySelection:
    case "A":
      match outcome:
        case "X": return "Z"
        case "Y": return "X"
        case "Z": return "Y"
    case "B":
      match outcome:
        case "X": return "X"
        case "Y": return "Y"
        case "Z": return "Z"
    case "C":
      match outcome:
        case "X": return "Y"
        case "Y": return "Z"
        case "Z": return "X"
                

def getSelectionPoints(selection):
  match selection:
    case "X": return 1
    case "Y": return 2
    case "Z": return 3

def play(enemySelection, mySelection):
  match (enemySelection):
    case "A": #ROCK
      match mySelection:
        case "X":
          return 3
        case "Y":
          return 6
        case "Z":
          return 0
      
    case "B": #PAPER
      match mySelection:
        case "X":
          return 0
        case "Y":
          return 3
        case "Z":
          return 6
        
    case "C": #SCISSORS
      match mySelection:
        case "X":
          return 6
        case "Y":
          return 0
        case "Z":
          return 3
      

print("Task 1 = ", task_1())
print("Task 2 = ", task_2())