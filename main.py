import argparse

from kigali_express.benchmark import run_benchmark
from kigali_express.data import load_drivers
from kigali_express.search import build_driver_hashmap, hashmap_search


def print_report(results, num_drivers, num_requests):
    line = "-" * 66
    print("\nKigali Express - Driver Lookup Benchmark")
    print(f"{num_drivers:,} drivers | {num_requests:,} requests\n")
    print(line)
    print(f"{'Method':<16}{'Setup (ms)':>12}{'All lookups (ms)':>18}{'Per lookup (us)':>18}")
    print(line)
    for r in results:
        print(f"{r['method']:<16}{r['setup_s'] * 1000:>12.3f}"
              f"{r['total_s'] * 1000:>18.3f}{r['per_lookup_us']:>18.3f}")
    print(line)

    baseline = results[0]["total_s"]
    for r in results[1:]:
        print(f"{r['method']:<16} is {baseline / r['total_s']:,.0f}x faster than Linear Search")
    print()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--requests", type=int, default=1000)
    args = parser.parse_args()

    drivers = load_drivers()
    results = run_benchmark(drivers, num_requests=args.requests)
    print_report(results, len(drivers), args.requests)

    drivers_by_id = build_driver_hashmap(drivers)
    driver = hashmap_search(drivers_by_id, "KGL-04217")
    print(f"Lookup KGL-04217 -> {driver['name']}, {driver['vehicle']}, {driver['sector']}\n")


if __name__ == "__main__":
    main()
