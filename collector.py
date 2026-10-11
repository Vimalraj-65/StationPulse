
import requests
from datetime import datetime, timezone

url = "https://gbfs.citibikenyc.com/gbfs/en/station_status.json"

print("StationPulse collector started!", flush=True)

try:
    response = requests.get(url, timeout=30)
    response.raise_for_status()

    data = response.json()
    stations = data["data"]["stations"]
    
import csv
import os

    print("Collection time:", datetime.now(timezone.utc), flush=True)
    print("Total stations:", len(stations), flush=True)
    print("First station:", stations[0], flush=True)

except Exception as e:
    print("ERROR:", repr(e), flush=True)
    raise
