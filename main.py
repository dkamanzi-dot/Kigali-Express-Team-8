import time
import json

DATA_FILE = "drivers.json"


def load_drivers(path=DATA_FILE):
    with open(path, "r") as f:
        return json.load(f)


def linear_search(drivers_list, target_id):
    for driver in drivers_list:
        if driver["driver_id"] == target_id:
            return driver
    return None


def binary_search(sorted_drivers_list, target_id):
    low = 0
    high = len(sorted_drivers_list) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_driver = sorted_drivers_list[mid]

        if mid_driver["driver_id"] == target_id:
            return mid_driver
        elif mid_driver["driver_id"] < target_id:
            low = mid + 1
        else:
            high = mid - 1

    return None


def build_driver_hashmap(drivers_list):
    driver_dict = {}
    for driver in drivers_list:
        driver_dict[driver["driver_id"]] = driver
    return driver_dict


def hashmap_search(driver_dict, target_id):
    return driver_dict.get(target_id)


def time_it(func, *args):
    start = time.time()
    result = func(*args)
    elapsed = time.time() - start
    return result, elapsed


drivers_list = load_drivers()
sorted_drivers_list = sorted(drivers_list, key=lambda d: d["driver_id"])
drivers_hashmap = build_driver_hashmap(drivers_list)
target_id = drivers_list[-1]["driver_id"]


methods = [
    ("Linear Search", linear_search, drivers_list),
    ("Binary Search", binary_search, sorted_drivers_list),
    ("HashMap Search", hashmap_search, drivers_hashmap),
]

times = {}

for label, func, data in methods:
    result, elapsed = time_it(func, data, target_id)
    times[label] = elapsed
    print(f"{label:<15}: {elapsed:.6f} sec  -> {result}")

print()
for label in ["Binary Search", "HashMap Search"]:
    speedup = times["Linear Search"] / times[label]
    print(f"{label} is {speedup:.1f}x faster")