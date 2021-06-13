import flask
import sys
from start_algorithm import startAlgo, stopAlgo
from flask import request, render_template, jsonify 
from flask_cors import CORS
from flask_mqtt import Mqtt


# sys.path.insert(1, '../algorithm')
# import start_algorithm


app = flask.Flask("__main__")
CORS(app)

data = {
    "bed_number": 0,
    "time_started": 0,
    "time_end": 0,
    "hfr_count": 0,
    "patient_accompanied": 0,
    "fall_risk_status": "tam"
}

@app.route("/")
def frontend():
    return flask.render_template("index.html")

@app.route("/patient-information", methods=["POST", "GET", "PATCH", "DELETE"])
def json():
    global data
    if request.method == "GET":
        return jsonify(data), 200
      
    elif request.method == "POST": 
        content = request.json
        data["bed_number"] = content["bed_number"]
        data["time_started"] = content["time_started"]
        data["patient_accompanied"] = content["patient_accompanied"]
        # startAlgo()
        return jsonify(data), 200

    elif request.method == "PATCH": 
        print("patch api called")
        #to update fall risk status 
        content = request.json
        print(content)
        data["fall_risk_status"] = content["fall_risk_status"]
        return jsonify(data), 200

    elif request.method == "DELETE": 
        data = {
            "bed_number": 0,
            "time_started": 0,
            "time_end": 0,
            "hfr_count": 0,
            "patient_accompanied": 0,
            "fall_risk_status": "low"
        }
        # stopAlgo()
        return "", 200

# Enable page refresh
@app.errorhandler(404)
def not_found(e):
    return render_template("index.html")

app.run(port=5000, debug=True)


# if __name__ == '__main__':
#     app.run()