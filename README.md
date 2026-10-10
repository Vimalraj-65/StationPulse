
import requests
from datetime import datetime, timezone

url = "https://gbfs.citibikenyc.com/gbfs/en/station_status.json"

response = requests.get(url, timeout=30)
response.raise_for_status()

data = response.json()
stations = data["data"]["stations"]

print("Collection time:", datetime.now(timezone.utc))
print("Total stations:", len(stations))
print("First station:", stations[0])

