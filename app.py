from flask import Flask, request, jsonify
from flask_cors import CORS

# ascii_alphabet = {
#     'A': [
#         [0, 1, 1, 1, 0],
#         [1, 0, 0, 0, 1],
#         [1, 1, 1, 1, 1],
#         [1, 0, 0, 0, 1],
#         [1, 0, 0, 0, 1]
#     ],
#     'B': [
#         [1, 1, 1, 1, 0],
#         [1, 0, 0, 0, 1],
#         [1, 1, 1, 1, 0],
#         [1, 0, 0, 0, 1],
#         [1, 1, 1, 1, 0]
#     ],
#     'C': [
#         [0, 1, 1, 1, 1],
#         [1, 0, 0, 0, 0],
#         [1, 0, 0, 0, 0],
#         [1, 0, 0, 0, 0],
#         [0, 1, 1, 1, 1]
#     ],
#     'D': [
#         [1, 1, 1, 1, 0],
#         [1, 0, 0, 0, 1],
#         [1, 0, 0, 0, 1],
#         [1, 0, 0, 0, 1],
#         [1, 1, 1, 1, 0]
#     ],
#     'E': [
#         [1, 1, 1, 1, 1],
#         [1, 0, 0, 0, 0],
#         [1, 1, 1, 1, 0],
#         [1, 0, 0, 0, 0],
#         [1, 1, 1, 1, 1]
#     ],
#     'F': [
#         [1, 1, 1, 1, 1],
#         [1, 0, 0, 0, 0],
#         [1, 1, 1, 1, 0],
#         [1, 0, 0, 0, 0],
#         [1, 0, 0, 0, 0]
#     ],
#     'G': [
#         [0, 1, 1, 1, 1],
#         [1, 0, 0, 0, 0],
#         [1, 0, 1, 1, 1],
#         [1, 0, 0, 0, 1],
#         [0, 1, 1, 1, 1]
#     ],
#     'H': [
#         [1, 0, 0, 0, 1],
#         [1, 0, 0, 0, 1],
#         [1, 1, 1, 1, 1],
#         [1, 0, 0, 0, 1],
#         [1, 0, 0, 0, 1]
#     ],
#     'I': [
#         [1, 1, 1, 1, 1],
#         [0, 0, 1, 0, 0],
#         [0, 0, 1, 0, 0],
#         [0, 0, 1, 0, 0],
#         [1, 1, 1, 1, 1]
#     ],
#     'J': [
#         [0, 0, 1, 1, 1],
#         [0, 0, 0, 0, 1],
#         [0, 0, 0, 0, 1],
#         [1, 0, 0, 0, 1],
#         [0, 1, 1, 1, 0]
#     ],
#     'K': [
#         [1, 0, 0, 0, 1],
#         [1, 0, 0, 1, 0],
#         [1, 1, 1, 0, 0],
#         [1, 0, 0, 1, 0],
#         [1, 0, 0, 0, 1]
#     ],
#     'L': [
#         [1, 0, 0, 0, 0],
#         [1, 0, 0, 0, 0],
#         [1, 0, 0, 0, 0],
#         [1, 0, 0, 0, 0],
#         [1, 1, 1, 1, 1]
#     ],
#     'M': [
#         [1, 0, 0, 0, 1],
#         [1, 1, 0, 1, 1],
#         [1, 0, 1, 0, 1],
#         [1, 0, 0, 0, 1],
#         [1, 0, 0, 0, 1]
#     ],
#     'N': [
#         [1, 0, 0, 0, 1],
#         [1, 1, 0, 0, 1],
#         [1, 0, 1, 0, 1],
#         [1, 0, 0, 1, 1],
#         [1, 0, 0, 0, 1]
#     ],
#     'O': [
#         [0, 1, 1, 1, 0],
#         [1, 0, 0, 0, 1],
#         [1, 0, 0, 0, 1],
#         [1, 0, 0, 0, 1],
#         [0, 1, 1, 1, 0]
#     ],
#     'P': [
#         [1, 1, 1, 1, 0],
#         [1, 0, 0, 0, 1],
#         [1, 1, 1, 1, 0],
#         [1, 0, 0, 0, 0],
#         [1, 0, 0, 0, 0]
#     ],
#     'Q': [
#         [0, 1, 1, 1, 0],
#         [1, 0, 0, 0, 1],
#         [1, 0, 0, 0, 1],
#         [1, 0, 1, 0, 1],
#         [0, 1, 1, 1, 1]
#     ],
#     'R': [
#         [1, 1, 1, 1, 0],
#         [1, 0, 0, 0, 1],
#         [1, 1, 1, 1, 0],
#         [1, 0, 1, 0, 0],
#         [1, 0, 0, 1, 0]
#     ],
#     'S': [
#         [0, 1, 1, 1, 1],
#         [1, 0, 0, 0, 0],
#         [0, 1, 1, 1, 0],
#         [0, 0, 0, 0, 1],
#         [1, 1, 1, 1, 0]
#     ],
#     'T': [
#         [1, 1, 1, 1, 1],
#         [0, 0, 1, 0, 0],
#         [0, 0, 1, 0, 0],
#         [0, 0, 1, 0, 0],
#         [0, 0, 1, 0, 0]
#     ],
#     'U': [
#         [1, 0, 0, 0, 1],
#         [1, 0, 0, 0, 1],
#         [1, 0, 0, 0, 1],
#         [1, 0, 0, 0, 1],
#         [0, 1, 1, 1, 0]
#     ],
#     'V': [
#         [1, 0, 0, 0, 1],
#         [1, 0, 0, 0, 1],
#         [1, 0, 0, 0, 1],
#         [0, 1, 0, 1, 0],
#         [0, 0, 1, 0, 0]
#     ],
#     'W': [
#         [1, 0, 0, 0, 1],
#         [1, 0, 0, 0, 1],
#         [1, 0, 1, 0, 1],
#         [1, 1, 0, 1, 1],
#         [1, 0, 0, 0, 1]
#     ],
#     'X': [
#         [1, 0, 0, 0, 1],
#         [0, 1, 0, 1, 0],
#         [0, 0, 1, 0, 0],
#         [0, 1, 0, 1, 0],
#         [1, 0, 0, 0, 1]
#     ],
#     'Y': [
#         [1, 0, 0, 0, 1],
#         [0, 1, 0, 1, 0],
#         [0, 0, 1, 0, 0],
#         [0, 0, 1, 0, 0],
#         [0, 0, 1, 0, 0]
#     ],
#     'Z': [
#         [1, 1, 1, 1, 1],
#         [0, 0, 0, 1, 0],
#         [0, 0, 1, 0, 0],
#         [0, 1, 0, 0, 0],
#         [1, 1, 1, 1, 1]
#     ]
# }


# Initialize Flask app
app = Flask(__name__)
CORS(app)

# initialize main class
class Lang:
    def __init__(self):
        self.command = ""
    
    # define parser
    def parse_code(self, code):
        self.command = code.split("|")


    def interpret_code(self, code):
        self.parse_code(code)
        com = self.command[0]
        
        if len(self.command) < 2:
            return "Error: Invalid input. Please check syntax page to ensure you have done it correctly."
        elif len(self.command) > 2:
            return "Error: '|' is not a valid character to use"
        
        match com:
            # print
            case "P":
                return self.command[1]
            # print reverse
            case "Pr":
                return self.command[1][::-1]
            # print reverse reverse
            case "Pri":
                return self.command[1][::-1][::-1]
            # print reverse reverse reverse
            case "Prin": 
                return self.command[1][::-1][::-1][::-1]
            # print reverse reverse reverse reverse
            case "Print": 
                return self.command[1][::-1][::-1][::-1][::-1]
            # add/sum
            case "+":
                values = self.command[1].split(' ')
                casted = [int(val) for val in values]
                return sum(casted)
            # subtract
            case "-":
                values = self.command[1].split(' ')
                casted = [int(val) for val in values]
                result = casted[0]
                for i in range(1, len(casted)):
                    result -= casted[i]
                return result
            case _:
                return "Error: Unknown command. Please check syntax page to ensure you have done it correctly."

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