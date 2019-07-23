from flask import Flask, render_template, request, escape
import requests
import json

app = Flask(__name__)


@app.route('/')
def hello():
    org = request.args.get("org", "")
    orgData = {"name": False}

    if org != "":
        response = requests.get(f'https://api.github.com/orgs/{escape(org)}')
        if response.status_code == 200:
            orgData = response.json()

    print(orgData["name"])
    print(orgData)

    if orgData["name"] == False:
        return render_template('search.html', orgData=orgData)
    else:
        return render_template('results.html', orgData=orgData)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3261)
