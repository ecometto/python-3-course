
# and, or, not

distance=int(input("insert distance"))
routes=int(input("insert quantity of routes"))
going = False

def go(d, r):
    global going
    if d < 1000 and r < 2:
        going = True 
    elif d > 1000 or r > 2:
        going = False
        
    if going == False:
        return "Do not Go"
    else:
        return "GO !!"

print(go(distance, routes))
print(f"the variable 'going' is : {going}. But not {not(going)}")