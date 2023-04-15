import json

from System_test.pe_info_utils import extract_sys_metrics, get_pos_engine


def get_mock_json():
    with open('test_data.json', 'r') as f:
        json_data = json.load(f)
    return json_data


def test_extract_sys_metrics():
    expected_result = {
        "cpuLoad": 0.18020304568527917,
        "memoryAllocated": 832569344,
        "memoryFree": 62914560,
        "memoryMax": 5746196480,
        "memoryUsed": 769654784,
        "networkLossRate": 2.340145902842528,
        "packetsPerSecond": 278.9647908516401,
        "qpeLossRate": 0,
        "udpRx": 35.1982421875,
        "udpTx": 0.02534250980896636
    }
    pos_engine = get_pos_engine(get_mock_json())
    assert extract_sys_metrics(pos_engine) == expected_result


def test_extract_sys_metrics_missing_field():
    pos_engine = {
        "cpuLoad": 12.34,
        "memoryAllocated": 56789,
        "memoryFree": 12345,
        "memoryMax": 67890,
        "memoryUsed": 55555,
        "networkLossRate": 0.05,
        "packetsPerSecond": 1234,
        "udpRx": 123,
        # The "qpeLossRate" field is missing
        "udpTx": 456
    }
    expected_result = {
        "cpuLoad": 12.34,
        "memoryAllocated": 56789,
        "memoryFree": 12345,
        "memoryMax": 67890,
        "memoryUsed": 55555,
        "networkLossRate": 0.05,
        "packetsPerSecond": 1234,
        "qpeLossRate": None,  # The value should be set to None
        "udpRx": 123,
        "udpTx": 456
    }
    assert extract_sys_metrics(pos_engine) == expected_result


def test_extract_sys_metrics_empty_pos_engine():
    pos_engine = {}
    expected_result = {
        "cpuLoad": None,
        "memoryAllocated": None,
        "memoryFree": None,
        "memoryMax": None,
        "memoryUsed": None,
        "networkLossRate": None,
        "packetsPerSecond": None,
        "qpeLossRate": None,
        "udpRx": None,
        "udpTx": None
    }
    assert extract_sys_metrics(pos_engine) == expected_result
