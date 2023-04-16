Introduction
------
This project sends a request to a provided API endpoint every 10 seconds,
filters the received JSON data to extract the required information,
and sends the filtered data to an InfluxDB database.


## Requirements

To use this script, you will need to have the following:

1. Python 3.10
2. An InfluxDB instance
3. A QPE API endpoint that returns JSON data containing system metrics
4. You will also need to create a `.env` file in the same directory as `main.py`,
and fill it with the following environment variables:
```
INFLUXDB_URL=<your InfluxDB URL>
INFLUXDB_ORG=<your InfluxDB organization>
INFLUXDB_TOKEN=<your InfluxDB token>
INFLUXDB_BUCKET=<your InfluxDB bucket>
QPE_API=<API endpoint>
```

## Usage

First install all the required dependencies from the `requirements.txt` file by running `pip install -r requirements.txt`
in your terminal. Then create the `.env` file and fill it according to the template above. 

Finally, run the `main.py` script.

## Code Explanation

* `sys_metrics` - getting a json from the API endpoint,
with `get_pos_engine` getting into nested JSON and finally with `extract_sys_metrics`
grabbing only those key-value pairs that are specified in `service_metrics` and saving it in the dictionary.

* `persist_sys_metrics_to_influx` - takes `extracted_data` from `extract_sys_metrics`, 
creates a list `data` that contains a template object to send to InfluxDB, and adds `extracted_data` into `fields`.

* In `data`, `measurements` is the name of the table in DB. If the name doesn't exist,
InfluxDB will create one, specified in the measurements.
* `tags` are optional, but adding more filtering criteria in the InfluxDB.

* Finally, the InfluxDBClient is called, and with `write_api` data is sent to the specified bucket .

## Tests Explanation

* `test_extract_sys_metrics` - loads mock JSON file, gets all the values from nested JSON `positioningEngine`,
and compares with the expected result

* `test_extract_sys_metrics_missing_field` - creating `pos_engine` dictionary with 1 missing field. The expected result
is a dictionary with missing field set to `None`.

* `test_extract_sys_metrics_empty_pos_engine` - creating an empty `pos_engine` dictionary and passing into a function.
The expected result is a dictionary with all fields set to `None`.

* `test_get_pos_engine` - test tests function `get_pos_engine` with mock JSON. Then checks if the dictionary returned by
`get_pos_engine` contains the expected values. Test passes if all the assertions pass.

* `test_get_pos_engine_empty_input` - testing function `get_pos_engine` when the empty dictionary is passed. It checks
if the result is dictionary and the length of the dictionary is 0.
