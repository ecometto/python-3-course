
# FOR loop
for n in range(1,11):
    if n == 2:
        continue
    if n == 8:
        break    
    print(n)
    
# multiplication table (x3)
for n in range(0,10):
    print("{} x 3 = {}".format(n, (n*3)))
    
# WHILE LOOP
index = 0
while index < 10:
    print(f"number {index} is less than 10")
    index = index + 1 
print("while loop finished")

num = 0
print("Even Numbers")
while num < 10:
    if num % 2 == 0:
        print(num)
    num = num +1 