
import requests
import csv
import os
from datetime import datetime, timezone

url = "https://gbfs.citibikenyc.com/gbfs/en/station_status.json"

print("StationPulse collector started!", flush=True)

try:
    response = requests.get(url, timeout=30)
    response.raise_for_status()

    data = response.json()
    stations = data["data"]["stations"]

    collection_time = datetime.now(timezone.utc).isoformat()

    print("Collection time:", collection_time, flush=True)
    print("Total stations:", len(stations), flush=True)
    print("First station:", stations[0], flush=True)

    os.makedirs("data", exist_ok=True)

    file_exists = os.path.exists("data/station_status.csv")
    fieldnames = [
        "collection_time",
        "station_id",
        "num_bikes_available",
        "num_docks_available",
        "is_installed",
        "is_renting",
        "is_returning"
    ]

    with open("data/station_status.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        for station in stations:
            row = {
                "collection_time": collection_time,
                "station_id": station.get("station_id"),
                "num_bikes_available": station.get("num_bikes_available"),
                "num_docks_available": station.get("num_docks_available"),
                "is_installed": station.get("is_installed"),
                "is_renting": station.get("is_renting"),
                "is_returning": station.get("is_returning")
            }

            writer.writerow(row)

    print("CSV saved successfully!", flush=True)
    print("File location: data/station_status.csv", flush=True)

except Exception as e:
    print("ERROR:", repr(e), flush=True)
    raise
