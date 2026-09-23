import unittest

from kigali_express.data import generate_drivers
from kigali_express.search import (
    binary_search,
    build_driver_hashmap,
    hashmap_search,
    linear_search,
)


class TestDriverSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.drivers = generate_drivers(count=500)
        cls.sorted_drivers = sorted(cls.drivers, key=lambda d: d["driver_id"])
        cls.driver_dict = build_driver_hashmap(cls.drivers)

    def test_hashmap_has_one_entry_per_driver(self):
        self.assertEqual(len(self.driver_dict), len(self.drivers))

    def test_all_methods_return_the_same_driver(self):
        for driver in self.drivers[::25]:
            target = driver["driver_id"]
            expected = linear_search(self.drivers, target)
            self.assertEqual(expected, driver)
            self.assertEqual(binary_search(self.sorted_drivers, target), expected)
            self.assertEqual(hashmap_search(self.driver_dict, target), expected)

    def test_missing_driver_returns_none(self):
        for search, data in [
            (linear_search, self.drivers),
            (binary_search, self.sorted_drivers),
            (hashmap_search, self.driver_dict),
        ]:
            self.assertIsNone(search(data, "KGL-99999"))

    def test_generated_data_is_reproducible(self):
        self.assertEqual(generate_drivers(count=50), generate_drivers(count=50))


if __name__ == "__main__":
    unittest.main()
