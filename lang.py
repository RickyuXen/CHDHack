# Aaron, Harpreet, Ricky - 

# Wrap functionality around class
class Lang:
    def __init__(self):
        self.command = ""
    
    def parse_code(self, code):
        self.command = code.split("|")
        print(self.command)

    def interpret_code(self, code):
        self.parse_code(code)
        com = self.command[0]
        match com:
            case "P":
                print(self.command[1])
            case "Pr":
                print(self.command[1][::-1])

print(""" Syntax:
      P|[input] -> prints out [input]
      Pr|[input] -> prints out [input] in reverse
""")
someCode = input()

test = Lang()
res = test.interpret_code(someCode)