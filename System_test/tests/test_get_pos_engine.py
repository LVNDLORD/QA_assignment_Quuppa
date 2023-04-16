import json

from System_test.pe_info_utils import get_pos_engine


def get_mock_json():
    with open('test_data.json', 'r') as f:
        json_data = json.load(f)
    return json_data


def test_get_pos_engine():
    json_data = get_mock_json()

    pos_engine = get_pos_engine(json_data)
    assert pos_engine["cpuLoad"] == 0.18020304568527917
    assert pos_engine["memoryAllocated"] == 832569344
    assert pos_engine["memoryFree"] == 62914560
    assert pos_engine["memoryMax"] == 5746196480
    assert pos_engine["memoryUsed"] == 769654784
    assert pos_engine["networkLossRate"] == 2.340145902842528
    assert pos_engine["packetsPerSecond"] == 278.9647908516401
    assert pos_engine["qpeLossRate"] == 0
    assert pos_engine["udpRx"] == 35.1982421875
    assert pos_engine["udpTx"] == 0.02534250980896636


def test_get_pos_engine_empty_input():
    result = get_pos_engine({})

    assert isinstance(result, dict)
    assert len(result) == 0

