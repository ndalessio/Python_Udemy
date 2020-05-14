import re 

print("Smart calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True

def doMath():
    global run # This allows me to have access and modify a global variable
    global previous
    equation = ""

    if equation == 0:
        equation = input("Enter equation: ")
    else:
        equation = input(str(previous))
    
    if equation == "quit":
        print("Goodbye, human")
        run = False
    else: 
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)
        
        if previous == 0:
            previous = eval(equation)
        else: 
            previous = eval(str(previous) + equation)
      
while run:
    doMath()