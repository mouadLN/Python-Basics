def add(a,b):
    return(a + b)

def sous(a,b):
    return(a - b)

def div(a,b):
    return(a / b)

def div(a,b):
    return(a / b)

def mul(a,b):
    return(a * b)

def carr(a,b):
    return(a ** b)



while True :
    a = int(input("enter the first number :"))
    b = int(input("enter the second number :"))
    opp = input("choose a operation ( + , - , * , / , **) ")

    if opp == "+" :
        print(add(a,b))
        
    if opp == "-" :
        print(sous(a,b))
        
    if opp == "*" :
        print(mul(a,b))
        
    if opp == "/" :
        if b == 0 :
            print("divising by 0 is not possible")
        else :
            print(div(a,b))
        
        
            
    if opp == "**" :
        print(carr(a,b))
    
        
    
    



