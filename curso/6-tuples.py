
# tuple is a set of inmutable values. This are represented between parentheses

oddNumbers = (1,3,5,7,9)
evenNumbers =(0,2,4,6,8)
variousThings =("hello", 4, False)
daysOfWeek = ("monday","tuesday","wednesday","thursday","friday")
weekendDays = ("saturday","sunday")

allDays = daysOfWeek + weekendDays

print(oddNumbers)
print(evenNumbers[1])
print(variousThings[-3])
print(evenNumbers[1:4])
print(evenNumbers[:4])
print(allDays)

print(evenNumbers.count(2))

if 2 in evenNumbers:
    print("2 IS A EVEN NUMBER")
else:
    print("2 is a ood number")