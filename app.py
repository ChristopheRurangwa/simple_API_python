from flask import Flask, jsonify

import getFunctionalities as Func

app = Flask(__name__)  # <-- creates the flask app


@app.route('/api/ping')
# Validation of the status_code, checks to see if it's ok; 200.
def check_response():
    data = {"success": True}
    data_error = {"error": "Tags parameter is required"}

    if Func.GetData.valid_requ('science') == 200:
        return jsonify(data)

    return jsonify(data_error)


@app.route('/api/posts')
# this method will call the method that return the api
def returns_requstd_Info():
    return Func.GetData.make_req('science', 'reads', 'asc')  # <-Error will be displayed if any of these is missing


if __name__ == "__main__":
    app.run()  # <-- start our server, basically starts the app
