from flask import Flask, render_template, request
from urllib.request import urlopen
import json

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    # import json

    # store the URL in url as
    # parameter for urlopen
    url = "https://cms.mlcs.xyz/api/view/program_sessions/all/"

    # store the response of URL
    response = urlopen(url)

    # storing the JSON response
    # from url in data
    data_json = json.loads(response.read())

    # print the json response
    cs_session = []
    for a in data_json:
        cs_session.append(a['Session_Title'])
    print(cs_session)
    return render_template("index.html", cs_session=cs_session)


@app.route("/user", methods=['POST', 'GET'])
def user():
    uname = request.form.get("uname")
    password = request.form.get("password")
    return render_template("user.html")


@app.route("/create", methods=['POST', 'GET'])
def create():
    url = "https://cms.mlcs.xyz/api/view/teaching_staff/all/"

    # store the response of URL
    response = urlopen(url)

    # storing the JSON response
    # from url in data
    data_json = json.loads(response.read())

    # print the json response
    teacher_name = []
    for b in data_json:
        teacher_name.append(b['teacher_name'])
    print(teacher_name)
    gname = request.form.get("gname")
    supervisor = request.form.get("supervisor")
    title = request.form.get("title")
    psw = request.form.get("psw")
    return render_template("create.html", teacher_name=teacher_name, gname=gname, supervisor=supervisor, title=title,
                           psw=psw)


@app.route("/group", methods=['POST', 'GET'])
def group():
    url = "https://cms.mlcs.xyz/api/view/students_of/BSIT-2016/all/"

    # store the response of URL
    response = urlopen(url)

    # storing the JSON response
    # from url in data
    data_json = json.loads(response.read())

    # print the json response
    student_name = []
    for c in data_json:
        student_name.append(c['student_name'])
    print(student_name)

    return render_template("group.html", student_name=student_name)
@app.route("/success", methods=['POST', 'GET'])
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)
