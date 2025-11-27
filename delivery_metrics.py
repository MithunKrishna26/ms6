# delivery_metrics.py
from prometheus_client import start_http_server, Summary, Gauge
import random
import time

# Metrics
total_deliveries = Gauge("total_deliveries", "Total number of deliveries")
pending_deliveries = Gauge("pending_deliveries", "Number of pending deliveries")
on_the_way_deliveries = Gauge("on_the_way_deliveries", "Number of deliveries on the way")
average_delivery_time = Summary("average_delivery_time", "Average delivery time in seconds")

def simulate_delivery():
    pending = random.randint(10, 50)
    on_the_way = random.randint(5, 25)
    delivered = random.randint(20, 80)
    avg_time = random.uniform(10, 50)

    total = pending + on_the_way + delivered

    # Update metrics
    total_deliveries.set(total)
    pending_deliveries.set(pending)
    on_the_way_deliveries.set(on_the_way)
    average_delivery_time.observe(avg_time)

    print(f"[DEBUG] total={total} pending={pending} on_the_way={on_the_way} avg_time={avg_time:.2f}s")

if __name__ == "__main__":
    start_http_server(8000)  # exposes /metrics
    print("[INFO] delivery_metrics listening on :8000/metrics")
    while True:
        simulate_delivery()
        time.sleep(1)
