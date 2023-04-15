from influxdb_client import InfluxDBClient, Point, WritePrecision
import os
from dotenv import load_dotenv

load_dotenv()


def get_db_client():
    return InfluxDBClient(
        url=os.getenv('INFLUXDB_URL'),
        token=os.getenv('INFLUXDB_TOKEN'),
        org=os.getenv('INFLUXDB_ORG'))


def persist_sys_metrics_to_influx(pe_info):
    data = [{
        "measurement": "filtered_system_metrics",
        "tags": {
            "performance": "vals",
        },
        "fields": pe_info
    }]
    get_db_client().write_api(bucket=os.getenv('INFLUXDB_BUCKET'), record=data)
    print(f"INFO: Data persisted: {data}")
