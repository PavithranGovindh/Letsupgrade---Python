# Printing the first armstrong number betn 1042000 to 702648265


print("Domo")

for number in range (1042000,702648265):
  calNumber = 0
  tempNumber = number
  while (number > 0):
    calNumber += ((number % 10) **3)
    number = int(number/10)
  if(tempNumber == calNumber):
    print("Armstrong number betwn the range : ", calNumber)
    break
  
print("Execution complete")