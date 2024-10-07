from flask import Flask, request, jsonify
from flask_cors import CORS
from run import run_model  

app = Flask(__name__)
CORS(app)  # allow requests from any origin

@app.route("/run-model", methods=["POST"])
def run_model_api():

    #get input
    data = request.get_json()
    sentence = data.get('sentence')
    word = data.get('word')
    irab = data.get('irab')
    
    result, analysis = run_model(sentence, word, irab)
    
    #return output
    return jsonify({
        'result': result,
        'analysis': analysis
    })

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(debug=True, host="0.0.0.0", port=5000)

