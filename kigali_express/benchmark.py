import random
import time

from .search import binary_search, build_driver_hashmap, hashmap_search, linear_search


def run_benchmark(drivers_list, num_requests=1000, seed=7):
    rng = random.Random(seed)
    requests = [rng.choice(drivers_list)["driver_id"] for _ in range(num_requests)]

    start = time.perf_counter()
    sorted_list = sorted(drivers_list, key=lambda d: d["driver_id"])
    sort_time = time.perf_counter() - start

    start = time.perf_counter()
    driver_dict = build_driver_hashmap(drivers_list)
    build_time = time.perf_counter() - start

    methods = [
        ("Linear Search", linear_search, drivers_list, 0.0),
        ("Binary Search", binary_search, sorted_list, sort_time),
        ("HashMap Search", hashmap_search, driver_dict, build_time),
    ]

    results = []
    for label, func, data, setup in methods:
        start = time.perf_counter()
        for target_id in requests:
            assert func(data, target_id) is not None, f"{label} missed {target_id}"
        total = time.perf_counter() - start
        results.append({
            "method": label,
            "setup_s": setup,
            "total_s": total,
            "per_lookup_us": total / num_requests * 1_000_000,
        })
    return results
