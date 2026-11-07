"""
Flatten the Daikibo telemetry JSON into a CSV file for Tableau,
then print a quick downtime summary to check the dashboard numbers.

How to run (from this folder):
    pip install pandas
    python flatten_telemetry.py

Input:  daikibo-telemetry-data.json.zip (included in this repository)
Output: daikibo-telemetry-data.csv
"""

import json
import zipfile

import pandas as pd

ZIP_FILE = "daikibo-telemetry-data.json.zip"
JSON_FILE = "daikibo-telemetry-data.json"
OUTPUT_CSV = "daikibo-telemetry-data.csv"

# Forage task rule: each machine reports every 10 minutes,
# so each "unhealthy" reading counts as 10 minutes of downtime
MINUTES_PER_READING = 10


def load_telemetry(zip_path: str, json_name: str) -> list:
    """Read the JSON file straight out of the zip file."""
    with zipfile.ZipFile(zip_path) as zf:
        with zf.open(json_name) as f:
            return json.load(f)


def flatten(records: list) -> pd.DataFrame:
    """Turn nested fields like location.city into flat columns like location_city."""
    df = pd.json_normalize(records, sep="_")
    # The timestamp is stored in milliseconds since 1970 (UTC)
    df["reading_time_utc"] = pd.to_datetime(df["timestamp"], unit="ms")
    return df


def downtime_summary(df: pd.DataFrame) -> None:
    """Print downtime minutes by factory, then by device type at the worst factory."""
    unhealthy = df[df["data_status"] == "unhealthy"]

    by_factory = (
        unhealthy.groupby(["location_city", "location_factory"])
        .size()
        .mul(MINUTES_PER_READING)
        .sort_values(ascending=False)
        .rename("downtime_minutes")
    )
    share = (by_factory / by_factory.sum() * 100).round(1).rename("pct_of_total")
    print("Downtime by factory:")
    print(pd.concat([by_factory, share], axis=1), "\n")

    worst_city = by_factory.index[0][0]
    by_device = (
        unhealthy[unhealthy["location_city"] == worst_city]
        .groupby("deviceType")
        .size()
        .mul(MINUTES_PER_READING)
        .sort_values(ascending=False)
        .rename("downtime_minutes")
    )
    print(f"Downtime by device type in {worst_city}:")
    print(by_device)


def main() -> None:
    records = load_telemetry(ZIP_FILE, JSON_FILE)
    df = flatten(records)

    print(f"Rows: {len(df):,}")
    print(f"Machines: {df['deviceID'].nunique()} across {df['location_factory'].nunique()} factories")
    print(f"Readings from {df['reading_time_utc'].min()} to {df['reading_time_utc'].max()} (UTC)\n")

    df.drop(columns="reading_time_utc").to_csv(OUTPUT_CSV, index=False)
    print(f"Saved {OUTPUT_CSV}\n")

    downtime_summary(df)


if __name__ == "__main__":
    main()
