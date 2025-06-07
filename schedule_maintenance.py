import requests
from datetime import datetime, timedelta

# === CONFIGURATION ===
PAGERDUTY_API_KEY = 'YOUR_API_KEY'
STATUS_PAGE_ID = 'YOUR_STATUS_PAGE_ID'
API_URL = f'https://api.pagerduty.com/status-pages/v1/pages/{STATUS_PAGE_ID}/maintenance'

# === USER INPUT ===
title = "Database and API Maintenance"
description = "Routine maintenance for database and API services."
start_time_str = "2025-06-10T02:00:00Z"  # UTC ISO format
end_time_str = "2025-06-10T03:00:00Z"    # UTC ISO format

# List of component IDs (replace with your actual component IDs)
components = [
    "component_id_database",
    "component_id_api"
]

# How far in advance to publish (in hours)
advance_notice_hours = 24

# === CALCULATE PUBLISH TIME ===
start_time = datetime.strptime(start_time_str, "%Y-%m-%dT%H:%M:%SZ")
publish_at = start_time - timedelta(hours=advance_notice_hours)
publish_at_str = publish_at.strftime("%Y-%m-%dT%H:%M:%SZ")

# === PAYLOAD ===
payload = {
    "title": title,
    "description": description,
    "start_time": start_time_str,
    "end_time": end_time_str,
    "publish_at": publish_at_str,
    "components": components
}

headers = {
    "Authorization": f"Token token={PAGERDUTY_API_KEY}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# === MAKE THE API REQUEST ===
response = requests.post(API_URL, json=payload, headers=headers)

if response.status_code == 201:
    print("Maintenance scheduled successfully!")
    print(response.json())
else:
    print(f"Failed to schedule maintenance: {response.status_code}")
    print(response.text)
