from flask import Flask, render_template, make_response, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", title="Home Info")

@app.route("/ask", methods=["POST"])
def info():
    resp = requests.get("https://api.tfl.gov.uk/Line/" + request.form["Line"] + "/Status")
    jresp = (resp.json())
    name = jresp[0]["name"]
    status = jresp[0]["lineStatuses"][0]["statusSeverityDescription"]
    reason = jresp[0]["lineStatuses"][0]["reason"]
    headers = {"Content-Type": "text/html"}
    return make_response(name + " - " + status + " - " + reason , 200, headers)


if __name__ == "__main__":
    app.run()