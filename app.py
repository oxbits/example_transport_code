import os
import json
import boto3
import datetime
from dotenv import load_dotenv, dotenv_values
from flask import Flask, request

app = Flask(__name__)
load_dotenv()
config = dotenv_values(".env")

DATA_DIR = "data/"
CACHE_MICROSECONDS = int(config["CACHE_MICROSECONDS"])

boto3_client_s3 = boto3.client("s3")
boto3_resource_s3 = boto3.resource("s3")


@app.route("/metric/<key>", methods=["POST"])
def create_metric_value(key):
    time_stamp = int(datetime.datetime.utcnow().timestamp() * 1_000_000)
    json_str = json.dumps(
        {
            "value": round(request.json["value"]),
        }
    )
    if config["USE_S3"].lower() == "false":
        file_path = os.path.join(".", DATA_DIR, f"{key}__{time_stamp}.json")
        with open(file_path, "w") as file:
            file.write(json_str)
    else:
        file_path = os.path.join(DATA_DIR, f"{key}/{time_stamp}.json")
        boto3_client_s3.put_object(
            Body=json_str, Bucket=config["S3_BUCKET"], Key=file_path
        )
    return "{}"


@app.route("/metric/<key>/sum")
def metric_sum(key):
    if config["USE_S3"].lower() == "false":
        return local_metric_sum(key)
    else:
        return s3_metric_sum(key)


def local_metric_sum(key):
    file_list = os.listdir(DATA_DIR)
    filtered_list = [item for item in file_list if key == item[: len(key)]]
    threshold = int(
        datetime.datetime.utcnow().timestamp() * 1_000_000 - CACHE_MICROSECONDS
    )
    sum_list = [
        item
        for item in filtered_list
        if int(item.split(".")[0].split("__")[-1]) > threshold
    ]
    delete_list = [
        os.remove(os.path.join(DATA_DIR, item))
        for item in filtered_list
        if int(item.split(".")[0].split("__")[-1]) <= threshold
    ]
    sum_list_values = [
        json.loads(open(os.path.join(DATA_DIR, item)).read())["value"]
        for item in sum_list
    ]
    result = json.dumps(
        {
            "value": round(sum(sum_list_values)),
        }
    )
    return result


def s3_metric_sum(key):
    filtered_list = [
        item
        for item in boto3_resource_s3.Bucket(config["S3_BUCKET"]).objects.filter(
            Prefix=os.path.join(DATA_DIR, f"{key}/")
        )
    ]
    threshold = int(
        datetime.datetime.utcnow().timestamp() * 1_000_000 - CACHE_MICROSECONDS
    )
    sum_list = [
        item
        for item in filtered_list
        if int(item.key.split(".")[0].split("/")[-1]) > threshold
    ]
    delete_list = [
        item.key
        for item in filtered_list
        if int(item.key.split(".")[0].split("/")[-1]) <= threshold
    ]
    if delete_list:
        boto3_client_s3.delete_objects(
            Bucket=config["S3_BUCKET"],
            Delete={
                "Objects": [
                    {
                        "Key": item,
                    }
                    for item in delete_list
                ],
            },
        )
    sum_list_values = [
        json.loads(item.get()["Body"].read())["value"] for item in sum_list
    ]
    result = json.dumps(
        {
            "value": round(sum(sum_list_values)),
        }
    )
    return result
