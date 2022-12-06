def task_1():
	with open("src/input4.txt") as f:
		lines = f.readlines()

		count = 0
		for line in lines:
			line = line.replace("\n", "")
			one, two = line.split(",")
			s1, e1 = one.split("-")
			s2,e2 = two.split("-")
			s1 = int(s1)
			e1 = int(e1)
			s2 = int(s2)
			e2 = int(e2)
			print(s1,e1,s2,e2)
			print(checkForCompleteOverlap(s1,e1,s2,e2))
			count += 1 if checkForCompleteOverlap(s1,e1,s2,e2) else 0
		return count
				

def checkForCompleteOverlap(s1,e1,s2,e2):
	return (s1 <= s2 and e1 >= e2) or (s2 <= s1 and e2 >= e1)

def task_2():
	with open("src/input4.txt") as f:
		lines = f.readlines()
		count = 0

		for line in lines:
			line = line.replace("\n", "")
			one, two = line.split(",")
			s1, e1 = one.split("-")
			s2,e2 = two.split("-")
			s1 = int(s1)
			e1 = int(e1)
			s2 = int(s2)
			e2 = int(e2)
			count += 1 if checkForAnyOverlap(s1,e1,s2,e2) else 0
		return count

def checkForAnyOverlap(s1,e1,s2,e2):
    return max(s1,s2) <= min(e1,e2) 


print(task_1())
print(task_2())