from flask import Flask
from flask import render_template, request, jsonify
import json

app = Flask(__name__)

users = []


@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        users.append(request.form.to_dict())
        # return json.dumps(users)
        # responce = app.response_class(
        #     response=json.dumps(users),
        #     status=201,
        #     mimetype='application/json',
        # )
        return jsonify(users)


@app.route('/handle_form', methods=['POST'])
def handle_form():
    # print(request.form)
    users.append([request.form.to_dict()])
    return json.dumps(users)


if __name__ == '__main__':
    app.run(debug=True)
