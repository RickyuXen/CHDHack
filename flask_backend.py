from flask import Flask, request, jsonify
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # This will allow all origins by default

# Your Lang class
class Lang:
    def __init__(self):
        self.command = ""
    
    def parse_code(self, code):
        self.command = code.split("|")
    
    def interpret_code(self, code):
        self.parse_code(code)
        com = self.command[0]
        
        if len(self.command) < 2:
            return "Error: Invalid input. Format should be 'P|[input]' or 'Pr|[input]'."
        
        match com:
            case "P":
                return self.command[1]
            case "Pr":
                return self.command[1][::-1]
            case _:
                return "Error: Unknown command. Valid commands are 'P' and 'Pr'."

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
