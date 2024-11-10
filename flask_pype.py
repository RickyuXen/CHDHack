from flask import Flask, request, jsonify
from flask_cors import CORS
import re

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # This will allow all origins by default

# Global variable to store variables
vars = ["Why did you try to get the 0th index?"]

# main class
class Lang:
    def __init__(self):
        self.command = ""
    
    # initialize parser
    def parse_code(self, code):
        # tokenize input
        self.command = code.split("|")

    #initialize interpreter
    def interpret_code(self, code):
        # call parser
        self.parse_code(code)
        com = self.command[0].strip()
        
        # if less than 2 tokens
        if len(self.command) < 2:
            return "Error: Invalid input. Please check syntax page to ensure you have done it correctly."
        # if more than 2 tokens
        elif len(self.command) > 2:
            return "Error: '|' is not a valid character to use"
        
        # trim off blank spaces from front and end
        self.command[1].strip()

        match com:
            # print function
            case "P":
                return self.command[1]
            # print reverse function
            case "Pr":
                return self.command[1][::-1]
            # print reverse reverse function
            case "Pri":
                return self.command[1][::-1][::-1]
            # print reverse reverse reverse function
            case "Prin": 
                return self.command[1][::-1][::-1][::-1]
            #print reverse reverse reverse reverse function
            case "Print": 
                return self.command[1][::-1][::-1][::-1][::-1]
            # addition function
            case "+":
                values = self.command[1].split(' ')
                casted = [int(val) for val in values]
                return sum(casted)
            # subtraction function
            case "-":
                values = self.command[1].split(' ')
                casted = [int(val) for val in values]
                result = casted[0]
                for i in range(1, len(casted)):
                    result -= casted[i]
                return result
            # store function
            case "S":  
                # Store variable in list
                vars.append(self.command[1])
                return f"Successfully stored value in variable slot {len(vars) - 1}"
            # call stored object function
            case command if (match := re.match(r"S(\d+)", command)):
            # Extract the index number
                varNumber = int(match.group(1))
                if 0 <= varNumber < len(vars):
                    return f"The variable stored is: {vars[varNumber]}"
                else:
                    return f"Error: No variable found at slot {varNumber}"
            case _:
                return "Error: Unknown command. Please check syntax page to ensure you have done it correctly."

# flask
@app.route('/process', methods=['POST'])
def process_code():
    data = request.get_json()

    if 'code' not in data:
        return jsonify({"error": "Missing 'code' in request body"}), 400

    lang_processor = Lang()
    result = lang_processor.interpret_code(data['code'])
    
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)