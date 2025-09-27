from flask import Flask, request, jsonify
from agent_router import run_agent
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    agent_type = data.get("type")   # "email" or "blog"
    input_text = data.get("input")  # the input content/topic

    result = run_agent(agent_type, input_text)
    return jsonify({"result": str(result)})

if __name__ == '__main__':
    app.run(debug=True)
