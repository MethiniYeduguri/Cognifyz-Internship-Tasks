#function for basic calculator
def basic_calculator(n1,n2,op):
    if(op=='+'):
        return (n1+n2)
    elif(op=='-'):
        return (n1-n2)
    elif(op=='*'):
        return (n1*n2)
    elif(op=='/'):
        if(n2==0):
            return("Can not be divided by Zero")
        return (n1/n2)
    elif(op=='%'):
        if(n2==0):
            return("Can not perform modulus by Zero")
        return (n1%n2)
    else:
        return("Invalid operator")

#input   
number1=float(input("Enter number1="))
number2=float(input("Enter number2="))
operator=input("Enter operator=")

#output
output=basic_calculator(number1,number2,operator)
print(f"{number1}{operator}{number2}={output}")