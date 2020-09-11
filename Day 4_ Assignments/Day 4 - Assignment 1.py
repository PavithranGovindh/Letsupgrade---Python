# Printing the first armstrong number betn 1042000 to 702648265


print("Domo")

for number in range (1042000,702648265):
  calNumber = 0
  tempNumber = number
  while (tempNumber > 0):
    calNumber += ((tempNumber % 10) **3)
    tempNumber //= 10)
  if(number == calNumber):
    print("Armstrong number betwn the range : ", calNumber)
    break
  
print("Execution complete")
