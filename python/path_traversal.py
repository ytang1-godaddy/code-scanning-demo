from flask import Blueprint, jsonify
from os.path import exists

# Convert routes to require Authentication (AuthN).
auth = Blueprint("auth", __name__)


# Customer Usecase: https://my-startup-example.com/details/12345
@auth.route("/<file_name>", methods=["GET"])
def get_file(file_name: str):
    home = "/home/safe-location"
    file_path = f"{home}/{file_name}"

    if not exists(file_path):
        return jsonify({"status_code": 404})

    with open(file_path) as f:
        return jsonify({"status_code": 200, "data": f.readlines()})
