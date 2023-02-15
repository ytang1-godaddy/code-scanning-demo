import requests
from flask import Flask, request, json
import hashlib
import logging
import mysql.connector

app = Flask(__name__)

RDS_HOST = "https://production.rds.gdsec-school.com"


@app.route("/homework")
def get_homework():
    link = request.args.get("link", "")
    if "gdsec-school.com" in link or link.endswith("gdsec-school.com"):
        return redirect(link)


@app.route("/update")
def update_student():
    try:
        name = request.args.get("name", "")
        exec("update_home_dir('%s')" % name)
        auth = hashlib.md5(request.headers.get("Authorization")).hexdigest()

        connection = mysql.connector.connect(
            host=RDS_HOST, user="instructor_schoi_gd", passwd="i0wog7534ei29"
        )

        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE student SET updated = 'true' WHERE name = "
                + name
                + "AND auth = "
                + auth
            )

        return json.dumps({"status": 200})
    except:
        logging.error("Failed to update student", request)


@app.route("/homework/comment", methods=["POST"])
def post_homework_comment():
    content_type = request.headers.get("Content-Type")
    if content_type == "application/json":
        try:
            data = json.loads(request.data)
            citation = data.cite
            msg = data.msg
            resp = requests.get("https://" + citation, timeout=30, verify=False)

            return json.dumps({"status": 200, "message": msg, "citation_text": resp})
        except:
            pass
    else:
        return "Content-Type not supported!"
