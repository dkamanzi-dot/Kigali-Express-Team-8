import json
import random
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "drivers.json"

FIRST_NAMES = ["Jean", "Aline", "Eric", "Claudine", "Patrick", "Divine", "Emmanuel", "Grace",
               "Olivier", "Diane", "Kenny", "Elvis", "Sandrine", "Yves", "Josiane", "Fabrice"]
LAST_NAMES = ["Uwimana", "Mugisha", "Niyonzima", "Uwase", "Habimana", "Mukamana", "Nshimiyimana",
              "Ingabire", "Kamanzi", "Dusabamahoro", "Mulinda", "Iradukunda", "Hakizimana"]
SECTORS = {
    "Gasabo": ["Remera", "Kimironko", "Kacyiru", "Gisozi", "Kinyinya"],
    "Kicukiro": ["Niboye", "Kagarama", "Gikondo", "Kanombe", "Gatenga"],
    "Nyarugenge": ["Nyamirambo", "Kiyovu", "Muhima", "Nyarugenge", "Kimisagara"],
}
VEHICLES = ["Motorcycle", "Bicycle", "Car"]


def generate_drivers(count=10_000, seed=42):
    rng = random.Random(seed)
    drivers = []
    for i in range(1, count + 1):
        district = rng.choice(list(SECTORS))
        drivers.append({
            "driver_id": f"KGL-{i:05d}",
            "name": f"{rng.choice(FIRST_NAMES)} {rng.choice(LAST_NAMES)}",
            "phone": f"+250 78{rng.randint(0, 9)} {rng.randint(100, 999)} {rng.randint(100, 999)}",
            "vehicle": rng.choices(VEHICLES, weights=[80, 12, 8])[0],
            "district": district,
            "sector": rng.choice(SECTORS[district]),
            "rating": round(rng.uniform(3.5, 5.0), 1),
            "available": rng.random() < 0.7,
        })
    rng.shuffle(drivers)
    return drivers


def save_drivers(drivers, path=DATA_FILE):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(drivers, indent=2), encoding="utf-8")


def load_drivers(path=DATA_FILE):
    path = Path(path)
    if not path.exists():
        save_drivers(generate_drivers(), path)
    return json.loads(path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    drivers = generate_drivers()
    save_drivers(drivers)
    print(f"Saved {len(drivers)} drivers to {DATA_FILE}")
