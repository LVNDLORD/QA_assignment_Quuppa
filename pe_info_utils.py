import datetime
import os
import time

import requests
from dotenv import load_dotenv

load_dotenv()

service_metrics = [
    "cpuLoad",
    "memoryAllocated",
    "memoryFree",
    "memoryMax",
    "memoryUsed",
    "networkLossRate",
    "packetsPerSecond",
    "qpeLossRate",
    "udpRx",
    "udpTx"
]


def get_sys_metrics():
    json_data = None

    while json_data is None:
        try:
            json_data = get_json_data()
        except (requests.exceptions.RequestException, ValueError):
            print_with_timestamp("ERROR: Failed to get system metrics from QPE API")
            time.sleep(10)

    json_data = get_json_data()
    pos_engine = get_pos_engine(json_data)
    sys_metrics = extract_sys_metrics(pos_engine)
    return sys_metrics


def get_json_data():
    response = requests.get(os.getenv('QPE_API'))
    response.raise_for_status()  # Raise exception for non-2XX status codes
    return response.json()


def get_pos_engine(json_data):
    return json_data.get('positioningEngine', {})


def extract_sys_metrics(pos_engine):
    extracted_data = {}
    for field in service_metrics:
        try:
            extracted_data[field] = pos_engine[field]
        except KeyError:
            print(f"WARNING: Key {field} is NOT found in JSON, field is set to None")
            extracted_data[field] = None
    return extracted_data


def print_with_timestamp(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{timestamp}] {message}")
