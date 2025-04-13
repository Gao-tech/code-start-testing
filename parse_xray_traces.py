import json
import csv
from pathlib import Path
from datetime import datetime

TRACE_DIR = "./xray_logs"
OUTPUT_CSV = "lambda_invocations.csv"

def extract_lambda_segments(trace_data):
    all_invocations = []
    # Handle both list and dict structures
    if isinstance(trace_data, dict):
        trace_summaries = trace_data.get("TraceSummaries", [])
    elif isinstance(trace_data, list):
        trace_summaries = trace_data
    else:
        trace_summaries = []

    for trace_summary in trace_summaries:
        duration = trace_summary.get("Duration", 0)
        start_time = trace_summary.get("StartTime")
        name = trace_summary.get("EntryPoint", {}).get("Name", "")
        
        cold_start = False
        for cause in trace_summary.get("ResponseTimeRootCauses", []):
            for service in cause.get("Services", []):
                for entity in service.get("EntityPath", []):
                    if entity.get("Name") in ["Init", "Initialization"]:
                        cold_start = True

        timestamp = datetime.fromisoformat(start_time).isoformat() if start_time else ""

        all_invocations.append({
            "function_name": name,
            "duration_secs": duration,
            "cold_start": cold_start,
            "start_time": timestamp
        })
    return all_invocations

def main():
    all_data = []
    for file in Path(TRACE_DIR).glob("trace*.json"):
        print(f"Parsing: {file}")
        with open(file) as f:
            trace_data = json.load(f)
            all_data.extend(extract_lambda_segments(trace_data))

    if not all_data:
        print("⚠️ No Lambda invocation data found.")
        return

    with open(OUTPUT_CSV, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["function_name", "duration_secs", "cold_start", "start_time"])
        writer.writeheader()
        writer.writerows(all_data)
    print(f"✅ Extracted {len(all_data)} entries to {OUTPUT_CSV}")

if __name__ == "__main__":
    main()