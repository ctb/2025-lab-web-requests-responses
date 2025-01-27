from flask import Flask, request, jsonify
import json
import traceback

app = Flask(__name__)

@app.route("/")
def index():
    return """Please fill out the following form:
<form method='GET' action='/do_submit'>
Input here: <input type="text" name="my_input"></input>
<input type="submit">
</form>
"""

@app.route("/do_submit", methods=["GET"])
def do_submit():
    form_val = request.args.get('my_input', '(none provided?!)')
    return f"Input was: {form_val}. <a href='./'>Return to form.</a>"

@app.route("/some_json", methods=["GET"])
def some_json():
    multiply_val = 0
    try:
        multiply_val = int(request.args["multiply"])
    except:
        traceback.print_exc()

    print('XXX', multiply_val, request.args)

    some_vals = {}
    some_vals['value1'] = 5
    some_vals['a list'] = ['hello', 'world']
    some_vals['a dict'] = dict(x=10, y=15)
    some_vals['multiply_by_5'] = multiply_val * 5

    print(some_vals)

    return jsonify(some_vals)
