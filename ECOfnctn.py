def in_code(code):
    code = input("Enter code:")
    if code == "*151#":
     return(in_code)
    else:
       print("Invalid MMI")
in_code("*151#") 

def validation (pin):
    pin = input("Enter pin")
    if pin == "1234":
       print("Successfully")
    else:
     validation(pin)  
     validation(1234)


     def add_numbers(a, b):
         sum = a + b
         return sum
     
     result = add_numbers(5, 7)
     print("The sum is:",result)
