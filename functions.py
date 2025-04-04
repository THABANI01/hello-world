# Online Python - IDE, Editor, Compiler, Interpreter

def mmi(code):
    mmicode = input("Please input the MMI code: ")
    if mmicode == code:
        pin = input("Enter your PIN: ")
        return validation(pin)
    else:
        print("Invalid MMI code")

def validation(pin):
    passcode = "1234"
    if passcode == pin:
        print("Success")
    else:
        print("Incorrect PIN. Try again.")
        new_pin = input("Enter your PIN: ")
        return validation(new_pin)
mmi("*151#")






