# Aaron, Harpreet, Ricky - 

# Wrap functionality around class
class Lang:
    def __init__(self, start, left_delim, right_delim):
        self.start = start
        self.left_delim = left_delim
        self.right_delim = right_delim

    def interpret_code(self, code):
        if code.startswith(self.start):
            # extract text
            try:
                text = code[2:].strip().strip(self.left_delim).strip(self.right_delim)
            except:
                print("Error: Unknown command")
        return text
    


someCode = "P <sup dog>"

test = Lang('P ', '<', '>')

res = test.interpret_code(someCode)
print(res)