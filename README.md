# PagerDuty Maintenance Scheduler

This script allows you to schedule maintenance events for one or more services (components) on your PagerDuty public status page. You can control how far in advance the maintenance appears to your users.

## Features

- Schedule maintenance for multiple services at once
- Set how far in advance the event appears on your status page
- Easy to configure and run

## Prerequisites

- Python 3.x
- [requests](https://pypi.org/project/requests/) library (`pip install requests`)
- PagerDuty API key with permissions to manage your status page
- Your PagerDuty status page ID
- Component IDs for the services you want to schedule

## How to Use

1. **Clone this repository:**

   ```bash
   git clone https://github.com/YOUR_USERNAME/pagerduty-maintenance-scheduler.git
   cd pagerduty-maintenance-scheduler
