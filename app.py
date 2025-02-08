from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    split_data = request.get_json()['chat'].split(' ')
    command = 'None'
    args = []

    if split_data[0][0] == '/':
        command = split_data[0][1:]
        args = split_data[1:]
    else:
        args = split_data
    return jsonify({'chat': f'{command}: ' + ' '.join(args)})

if __name__ == '__main__':
    app.run(debug=True)
