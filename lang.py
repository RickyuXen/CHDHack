# Aaron, Harpreet, Ricky - 

def interpret_code(code):
    if code.startswith("P "):
        # extract text
        text = code[2:].strip().strip('<').strip('>')
        print(text)
    else:
        print("Error: Unknown command")

someCode = "P <sup dog>"

interpret_code(someCode)