from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/collect_data', methods=['POST'])
def collect_data():
    data = request.json
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
