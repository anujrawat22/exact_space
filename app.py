from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit-json', methods=['POST'])
def submit_json():
    try:
        data = request.get_json()
        submitted_json = data.get('json_data', '')
        return jsonify({'message': 'JSON submitted successfully', 'data': submitted_json})
    except Exception as e:
        print(e)
        return jsonify({'error': 'Invalid JSON data'}), 400

if __name__ == '__main__':
    app.run(debug=True)
