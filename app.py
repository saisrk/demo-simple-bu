from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/greet', methods=['POST'])
def greet():
    data = request.get_json()
    # BUG: Missing null check - will raise KeyError if 'name' is missing
    # comment for fixing
    # One more change here
    name = data['name']
    return jsonify({'message': f'Hello, {name}!'})

if __name__ == '__main__':
    app.run(debug=True)
