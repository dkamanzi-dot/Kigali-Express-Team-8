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
