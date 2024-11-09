# Aaron, Harpreet, Ricky - 

# Wrap functionality around class
class Lang:
    def __init__(self, left_delim, right_delim):
        self.left_delim = left_delim
        self.right_delim = right_delim

    def interpret_code(self, code):
        if code.startswith('P '):
            # extract text
            try:
                text = code[2:].strip().strip(self.left_delim).strip(self.right_delim)
                return text
            except:
                print("Error: Unknown command")
        else:
                print("Error: Unknown command")

print(""" Syntax:
      P <[input]> -> prints out [input]
""")
someCode = input()

test = Lang('<', '>')

res = test.interpret_code(someCode)
print(res)