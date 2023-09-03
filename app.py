from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def json_form():
    if request.method == 'POST':
        try:
            submitted_json = request.form['json_data']
            return jsonify({'message': 'JSON submitted successfully', 'data': submitted_json})
        except:
            return jsonify({'error': 'Invalid JSON data'})

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
