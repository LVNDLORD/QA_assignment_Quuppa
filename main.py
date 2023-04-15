import time
import schedule
from pe_info_utils import get_sys_metrics, print_with_timestamp
from influx_client import persist_sys_metrics_to_influx


def handle_pe_info_data():
    print_with_timestamp("INFO: running handle_pe_info_data")
    start_time = time.time()

    sys_metrics = get_sys_metrics()
    persist_sys_metrics_to_influx(sys_metrics)

    end_time = time.time()
    execution_time_ms = (end_time - start_time) * 1000
    print(f"INFO: Execution time: {execution_time_ms:.2f} ms")


if __name__ == '__main__':
    schedule.every(10).seconds.do(handle_pe_info_data)
    while True:
        schedule.run_pending()
        time.sleep(1) #to get less load for CPU
