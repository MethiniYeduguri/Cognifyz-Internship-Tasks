#function to convert fahrenheit to celsius
def f_to_c(num):
    c=(num-32)*5/9
    return(f"{c:.2f}°C")

#function to convert celsius to fahrenheit
def c_to_f(num):
    f=(num*9/5)+32
    return(f"{f:.2f}°F")

#function to find the input unit of measurement
def unit_measurement(temp):
    dup_temp=temp.strip()
    num_part=''
    char_part=''
    for i in dup_temp:
        if(not(i.isalpha())):
            num_part+=i
        else:
            char_part+=i
    number=float(num_part)
    unit=char_part.lower()
    if(unit=='c'):
        return c_to_f(number)
    else:
        return f_to_c(number)

#input
temperature=input("Enter temperature with units (Ex:- 20 C)=")
output=unit_measurement(temperature)

#output
print(output)